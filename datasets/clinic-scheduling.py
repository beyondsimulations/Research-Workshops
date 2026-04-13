# /// script
# requires-python = ">=3.12"
# dependencies = ["numpy>=2", "pandas>=2"]
# ///
"""Generate synthetic rehabilitation clinic scheduling instances.

Writes three instances (small / medium / large) to
``datasets/clinic-scheduling/<size>/`` with seven CSV files each:

    patients.csv, staff.csv, qualifications.csv, rooms.csv,
    therapies.csv, therapy_plans.csv, availability.csv

Run with:

    uv run datasets/clinic-scheduling.py

Produced instances cover the five planning dimensions of the seminar topic
(time, rooms, staff, patients, therapies) and are deterministic via a fixed
seed, so re-running overwrites the same files byte-for-byte.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd


# --------------------------------------------------------------------------- #
# Constants                                                                   #
# --------------------------------------------------------------------------- #

SEED = 42
OUTPUT_ROOT = Path(__file__).parent / "clinic-scheduling"

# Time structure: 7-day horizon, 30-min slots covering 07:00-18:00.
DAYS = 7
SLOTS_PER_DAY = 22  # 07:00 .. 18:00 in 30-min slots

# Two staff shifts per day (no night shift for therapy).
# Early: 07:00-13:00 (slots 0-11). Late: 12:00-18:00 (slots 10-21).
# The 2-slot overlap models patient handover.
SHIFT_SLOTS: dict[str, list[int]] = {
    "early": list(range(0, 12)),
    "late": list(range(10, 22)),
}
SHIFT_NAMES: tuple[str, ...] = ("early", "late")
HOURS_PER_SHIFT = 6


@dataclass(frozen=True)
class Therapy:
    code: str
    name: str
    duration_slots: int
    required_room_types: tuple[str, ...]
    required_qualification: str
    is_group: bool


THERAPY_CATALOG: tuple[Therapy, ...] = (
    Therapy("PT", "Physiotherapy",        2, ("gym", "treatment"), "PT_LICENSE", False),
    Therapy("OT", "Occupational Therapy", 2, ("treatment",),       "OT_LICENSE", False),
    Therapy("ST", "Speech Therapy",       1, ("treatment",),       "ST_LICENSE", False),
    Therapy("AT", "Aquatic Therapy",      2, ("pool",),            "AT_LICENSE", False),
    Therapy("MA", "Massage",              1, ("treatment",),       "MA_LICENSE", False),
    Therapy("GG", "Group Gymnastics",     2, ("gym",),             "PT_LICENSE", True),
)
THERAPY_BY_CODE: dict[str, Therapy] = {t.code: t for t in THERAPY_CATALOG}
QUALIFICATIONS: tuple[str, ...] = tuple(
    sorted({t.required_qualification for t in THERAPY_CATALOG})
)

# Diagnosis -> therapy pool a patient may receive.
DIAGNOSIS_PROFILES: dict[str, tuple[str, ...]] = {
    "orthopedic": ("PT", "MA", "GG", "OT"),
    "neurologic": ("PT", "OT", "ST", "MA"),
    "cardiac":    ("PT", "GG", "AT", "MA"),
}
DIAGNOSIS_WEIGHTS = (0.5, 0.3, 0.2)  # matches insertion order above

INSTANCE_SIZES: dict[str, dict[str, int]] = {
    "small":  {"patients": 15,  "staff": 6,  "rooms": 5,  "seed_offset": 0},
    "medium": {"patients": 40,  "staff": 15, "rooms": 10, "seed_offset": 1},
    "large":  {"patients": 100, "staff": 35, "rooms": 20, "seed_offset": 2},
}


# --------------------------------------------------------------------------- #
# Generators                                                                  #
# --------------------------------------------------------------------------- #

def generate_patients(rng: np.random.Generator, n: int) -> pd.DataFrame:
    """IDs, stay window, and diagnosis group per patient."""
    diagnoses = rng.choice(
        list(DIAGNOSIS_PROFILES),
        size=n,
        p=list(DIAGNOSIS_WEIGHTS),
    )
    admission = rng.integers(low=0, high=4, size=n)       # day 0..3
    stay_length = rng.integers(low=3, high=8, size=n)     # 3..7 days
    discharge = np.minimum(admission + stay_length - 1, DAYS - 1)
    return pd.DataFrame({
        "patient_id":      [f"P{i + 1:03d}" for i in range(n)],
        "admission_day":   admission.astype(int),
        "discharge_day":   discharge.astype(int),
        "diagnosis_group": [str(d) for d in diagnoses],
    })


def generate_staff(rng: np.random.Generator, n: int) -> pd.DataFrame:
    weekly_hours = rng.choice([20, 30, 40], size=n, p=[0.2, 0.3, 0.5])
    return pd.DataFrame({
        "staff_id":     [f"T{i + 1:02d}" for i in range(n)],
        "role":         ["therapist"] * n,
        "weekly_hours": weekly_hours.astype(int),
    })


def generate_rooms(rng: np.random.Generator, n: int) -> pd.DataFrame:
    """Mix of treatment / gym / pool with realistic ratios and capacities."""
    num_pool = max(1, round(n * 0.1))
    num_gym = max(1, round(n * 0.3))
    num_treatment = n - num_pool - num_gym
    if num_treatment < 1:
        num_treatment = 1
        num_gym = max(1, n - num_pool - 1)

    types: list[str] = (
        ["treatment"] * num_treatment
        + ["gym"] * num_gym
        + ["pool"] * num_pool
    )
    rng.shuffle(types)  # avoid clustered IDs by type

    capacities: list[int] = []
    for t in types:
        if t == "treatment":
            capacities.append(1)
        elif t == "gym":
            capacities.append(int(rng.integers(2, 9)))  # 2..8
        else:  # pool
            capacities.append(int(rng.integers(1, 5)))  # 1..4

    return pd.DataFrame({
        "room_id":   [f"R{i + 1:02d}" for i in range(n)],
        "room_type": types,
        "capacity":  capacities,
    })


def generate_therapy_plans(
    rng: np.random.Generator, patients: pd.DataFrame
) -> pd.DataFrame:
    """Per-patient prescribed therapies drawn from the diagnosis profile."""
    rows: list[dict] = []
    for _, p in patients.iterrows():
        stay = int(p.discharge_day - p.admission_day + 1)
        pool = list(DIAGNOSIS_PROFILES[p.diagnosis_group])
        # 2..4 distinct therapy types per patient.
        k = int(rng.integers(2, min(5, len(pool) + 1)))
        chosen = rng.choice(pool, size=k, replace=False)
        for code in chosen:
            # sessions_required ~ 0.6 * stay .. stay (rounded, min 1).
            lo = max(1, int(round(0.6 * stay)))
            hi = max(lo + 1, stay + 1)
            sessions = int(rng.integers(lo, hi))
            rows.append({
                "patient_id":        p.patient_id,
                "therapy_code":      str(code),
                "sessions_required": sessions,
            })
    return pd.DataFrame(rows)


def generate_qualifications(
    rng: np.random.Generator,
    staff: pd.DataFrame,
    therapy_plans: pd.DataFrame,
) -> pd.DataFrame:
    """Assign 1-3 qualifications per therapist, biased toward demand.

    Computes per-qualification demand (in slot-hours) from the generated
    therapy plans and targets a primary-qualification distribution matching
    that demand. Each therapist then receives 0-2 additional random
    qualifications. Finally, a coverage pass adds extra holders to any
    qualification whose effective capacity is below ``1.3 * demand``.
    """
    n_staff = len(staff)

    demand_slots: dict[str, float] = {q: 0.0 for q in QUALIFICATIONS}
    for _, row in therapy_plans.iterrows():
        t = THERAPY_BY_CODE[row.therapy_code]
        demand_slots[t.required_qualification] += row.sessions_required * t.duration_slots

    total_demand = sum(demand_slots.values())

    # Target number of therapists holding each qualification as a primary.
    primary_targets: dict[str, int] = {}
    for q, d in demand_slots.items():
        share = (
            d / total_demand if total_demand > 0 else 1 / len(QUALIFICATIONS)
        )
        share = max(share, 0.05)  # every qualification gets at least a small share
        primary_targets[q] = max(1, int(round(share * n_staff)))

    # Scale back if the sum exceeds the number of staff.
    total_targets = sum(primary_targets.values())
    if total_targets > n_staff:
        scale = n_staff / total_targets
        primary_targets = {q: max(1, int(round(v * scale))) for q, v in primary_targets.items()}

    # Build the primary assignment pool, pad to n_staff, shuffle.
    primary_pool: list[str] = []
    for q, count in primary_targets.items():
        primary_pool.extend([q] * count)
    while len(primary_pool) < n_staff:
        primary_pool.append(str(rng.choice(QUALIFICATIONS)))
    primary_pool = primary_pool[:n_staff]
    rng.shuffle(primary_pool)

    rows: list[dict] = []
    for staff_id, primary in zip(staff.staff_id, primary_pool):
        quals: set[str] = {str(primary)}
        n_extra = int(rng.choice([0, 1, 2], p=[0.3, 0.5, 0.2]))
        for _ in range(n_extra):
            quals.add(str(rng.choice(QUALIFICATIONS)))
        for q in sorted(quals):
            rows.append({"staff_id": staff_id, "qualification": q})

    qual_df = pd.DataFrame(rows)

    # Coverage pass: if demand for a qualification exceeds ~1.3x effective
    # capacity, add more holders until the budget is met or every therapist
    # holds it. Effective capacity is approximated as
    # (sum of holders' weekly_hours * 2 slots/hour) * 0.35 (attention split).
    def holders_of(q: str) -> np.ndarray:
        return qual_df.loc[qual_df.qualification == q, "staff_id"].unique()

    extras: list[dict] = []
    for q in QUALIFICATIONS:
        holders = holders_of(q)
        if len(holders) == 0:
            chosen_id = str(staff.staff_id.iloc[int(rng.integers(0, n_staff))])
            extras.append({"staff_id": chosen_id, "qualification": q})
            qual_df = pd.concat([qual_df, pd.DataFrame(extras[-1:])], ignore_index=True)
            holders = holders_of(q)

        def effective(holders: np.ndarray) -> float:
            supply_slots = float(
                staff.loc[staff.staff_id.isin(holders), "weekly_hours"].sum()
            ) * 2
            return supply_slots * 0.35

        while effective(holders) < 1.3 * demand_slots[q] and len(holders) < n_staff:
            remaining = [s for s in staff.staff_id if s not in holders]
            new_id = str(rng.choice(remaining))
            extras.append({"staff_id": new_id, "qualification": q})
            qual_df = pd.concat([qual_df, pd.DataFrame(extras[-1:])], ignore_index=True)
            holders = holders_of(q)

    return (
        qual_df.drop_duplicates()
        .sort_values(["staff_id", "qualification"])
        .reset_index(drop=True)
    )


def generate_availability(rng: np.random.Generator, staff: pd.DataFrame) -> pd.DataFrame:
    """One row per (staff, day) with shift name or 'off'.

    Weekend days (5, 6) receive reduced weighting (~40% of weekday weight),
    and the number of shifts per week roughly matches each therapist's
    contracted ``weekly_hours``.
    """
    rows: list[dict] = []
    day_weights = np.array([1.0] * 5 + [0.35, 0.35])
    day_weights /= day_weights.sum()

    for _, s in staff.iterrows():
        target_shifts = max(3, min(7, round(s.weekly_hours / HOURS_PER_SHIFT)))
        worked_days = set(
            int(d) for d in rng.choice(DAYS, size=target_shifts, replace=False, p=day_weights)
        )
        for d in range(DAYS):
            shift = str(rng.choice(SHIFT_NAMES)) if d in worked_days else "off"
            rows.append({"staff_id": s.staff_id, "day": d, "shift": shift})
    return pd.DataFrame(rows)


def therapy_catalog_df() -> pd.DataFrame:
    return pd.DataFrame([
        {
            "therapy_code":           t.code,
            "name":                   t.name,
            "duration_slots":         t.duration_slots,
            "required_room_types":    "|".join(t.required_room_types),
            "required_qualification": t.required_qualification,
            "is_group":               t.is_group,
        }
        for t in THERAPY_CATALOG
    ])


# --------------------------------------------------------------------------- #
# Orchestration                                                               #
# --------------------------------------------------------------------------- #

def write_instance(name: str, cfg: dict[str, int]) -> dict[str, int]:
    rng = np.random.default_rng(SEED + cfg["seed_offset"])
    out = OUTPUT_ROOT / name
    out.mkdir(parents=True, exist_ok=True)

    patients       = generate_patients(rng, cfg["patients"])
    staff          = generate_staff(rng, cfg["staff"])
    rooms          = generate_rooms(rng, cfg["rooms"])
    therapies      = therapy_catalog_df()
    therapy_plans  = generate_therapy_plans(rng, patients)
    qualifications = generate_qualifications(rng, staff, therapy_plans)
    availability   = generate_availability(rng, staff)

    patients.to_csv(out / "patients.csv", index=False)
    staff.to_csv(out / "staff.csv", index=False)
    qualifications.to_csv(out / "qualifications.csv", index=False)
    rooms.to_csv(out / "rooms.csv", index=False)
    therapies.to_csv(out / "therapies.csv", index=False)
    therapy_plans.to_csv(out / "therapy_plans.csv", index=False)
    availability.to_csv(out / "availability.csv", index=False)

    return {
        "patients":       len(patients),
        "staff":          len(staff),
        "rooms":          len(rooms),
        "therapies":      len(therapies),
        "plans":          len(therapy_plans),
        "quals":          len(qualifications),
        "availability":   len(availability),
        "total_sessions": int(therapy_plans.sessions_required.sum()),
    }


def main() -> None:
    print(f"Writing instances to {OUTPUT_ROOT}/\n")
    for name, cfg in INSTANCE_SIZES.items():
        stats = write_instance(name, cfg)
        line = ", ".join(f"{k}={v}" for k, v in stats.items())
        print(f"[{name:>6}] {line}")
    print("\nDone.")


if __name__ == "__main__":
    main()

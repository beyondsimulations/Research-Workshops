# Rehabilitation clinic scheduling dataset

Synthetic data for the seminar *"Shift Scheduling for Rehabilitation Clinics
with Room and Patient Assignments"*. Three instances, one schema.

| Instance | Patients | Staff | Rooms | Plans | Sessions |
| -------- | -------: | ----: | ----: | ----: | -------: |
| small    |       15 |     6 |     5 |    50 |      192 |
| medium   |       40 |    15 |    10 |   125 |      460 |
| large    |      100 |    35 |    20 |   308 |    1,111 |

## Time

7 days (`0..6`); days 5 and 6 are the weekend. Each day has 22 half-hour
slots from 07:00 to 18:00. Therapists work one of two shifts per day, or
they are off:

- `early`: slots 0–11 (07:00–13:00)
- `late`:  slots 10–21 (12:00–18:00)

The two overlapping slots are a handover buffer. A session cannot span it.

## Files

UTF-8 CSVs with a header row. One folder per instance.

`patients.csv`: `patient_id`, `admission_day`, `discharge_day` (both in 0..6),
`diagnosis_group` (`orthopedic` / `neurologic` / `cardiac`).

`staff.csv`: `staff_id`, `role` (always `therapist`), `weekly_hours` in {20, 30, 40}.

`qualifications.csv` (long): `staff_id`, `qualification`, one of `PT_LICENSE`,
`OT_LICENSE`, `ST_LICENSE`, `AT_LICENSE`, `MA_LICENSE`. A therapist can only
deliver a therapy whose license they hold.

`rooms.csv`: `room_id`, `room_type` (`treatment` / `gym` / `pool`), `capacity`.
Treatment rooms hold 1 patient, gyms 2–8, pools 1–4.

`therapies.csv`: the six therapies, with `therapy_code`, `name`,
`duration_slots`, `required_room_types` (pipe-separated),
`required_qualification`, `is_group`. Codes: `PT` physiotherapy, `OT`
occupational therapy, `ST` speech therapy, `AT` aquatic therapy, `MA` massage,
`GG` group gymnastics. Only `GG` is a group therapy. The rest are 1-on-1.

`therapy_plans.csv` (long): `patient_id`, `therapy_code`, `sessions_required`.
Every required session must fall inside the patient's stay window.

`availability.csv` (long): one row per `(staff_id, day)` with `shift` in
`{early, late, off}`.

## The problem

Assign every required session to a `(day, slot, room, therapist)`, plus a
set of patients for group sessions, so that:

1. Every row in `therapy_plans.csv` is delivered `sessions_required` times.
2. Sessions fall inside the patient's stay window.
3. The room's `room_type` matches the therapy's `required_room_types`.
4. The therapist holds the required qualification.
5. The slots fall inside the therapist's shift that day.
6. No therapist, room, or patient is double-booked. Group sessions may share
   a room up to `capacity`.
7. A session fills `duration_slots` contiguous slots and cannot span the
   shift handover.

Choose whatever objective makes sense for your model.

## Loading in Julia

```julia
using CSV, DataFrames

instance = joinpath("datasets", "clinic-scheduling", "small")

patients       = CSV.read(joinpath(instance, "patients.csv"),       DataFrame)
staff          = CSV.read(joinpath(instance, "staff.csv"),          DataFrame)
qualifications = CSV.read(joinpath(instance, "qualifications.csv"), DataFrame)
rooms          = CSV.read(joinpath(instance, "rooms.csv"),          DataFrame)
therapies      = CSV.read(joinpath(instance, "therapies.csv"),      DataFrame)
therapy_plans  = CSV.read(joinpath(instance, "therapy_plans.csv"),  DataFrame)
availability   = CSV.read(joinpath(instance, "availability.csv"),   DataFrame)
```

Swap `"small"` for `"medium"` or `"large"`.

## Difficulty

These instances are intentionally easy. Supply-to-demand ratios are between
roughly 2.5× and 8× for every qualification and every room type, and a plain
greedy placement already solves all three sizes. A feasible schedule
definitely exists, the exercise is finding a good one.

The tightest resources are the pool (aquatic therapy) and the gyms (group
gymnastics). If `large/` is not challenging enough, write me and I will
generate a harder variant for you: fewer pools and gyms, denser plans,
narrower stay windows, a longer horizon. The file schema stays the same, so
your loading code keeps working.

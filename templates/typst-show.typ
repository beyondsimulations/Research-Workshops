// Minimal typst-show.typ that skips the default title page
#show: doc => {
  // Apply document settings without rendering a title
  set text(lang: "en")
  set heading(numbering: "1.1")
  doc
}

# Subject Question Bank

This repository includes a generated question bank file:

- `subject_question_bank.csv`

## What it contains

- All subjects from your provided list.
- `200` multiple-choice questions per subject.
- `4` options per question (`option_a`..`option_d`).
- `correct_option` field containing the correct choice letter.
- Progression tags in `difficulty` column:
  - Questions `1-70`: Easy
  - Questions `71-140`: Medium
  - Questions `141-200`: Hard

## Ordering

The `subject_order` column places common/core subjects first (e.g., Mathematics, Physics, Chemistry, Biology, Computer Science, Medicine, Law), then the remaining subjects.

## Regeneration

Run:

```bash
python3 generate_subject_question_bank.py
```

This will regenerate `subject_question_bank.csv`.

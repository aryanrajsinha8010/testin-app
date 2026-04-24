# Subject Question Bank (Rewritten)

This project now provides a **rewritten** question bank with significantly more varied question patterns.

## Output file

- `subject_question_bank.csv`

## Coverage and format

- Includes all subjects listed in your prompt.
- `200` MCQs per subject.
- Each question has `4` options and one `correct_option` (`A`/`B`/`C`/`D`).
- Difficulty progression:
  - Q1–Q70: Easy
  - Q71–Q140: Medium
  - Q141–Q200: Hard

## Syllabus orientation

The generator is designed around Class 11/12 + first-year college style syllabus coverage:

- Core subject topic maps for high-demand subjects (Physics, Chemistry, Biology, Mathematics, Computer Science, Law, Medicine, Electrical Engineering, Software Engineering).
- Category-level topic pools for the remaining subjects.
- Mixed conceptual, numerical, interpretation, methodology, and application-style questions.

## Regenerate

```bash
python3 generate_subject_question_bank.py
```

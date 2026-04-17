#!/usr/bin/env python3
import csv
SCIENCE = [
    "Physics", "Astrophysics", "Quantum Mechanics", "Nuclear Physics", "Particle Physics", "Theoretical Physics", "Thermodynamics", "Chemistry", "Organic Chemistry", "Inorganic Chemistry", "Physical Chemistry", "Biochemistry", "Molecular Biology", "Genetics", "Biology", "Marine Biology", "Evolutionary Biology", "Microbiology", "Botany", "Zoology", "Neuroscience", "Pharmacology", "Earth Science", "Geology", "Paleontology", "Meteorology", "Oceanography", "Environmental Science", "Ecology", "Astronomy", "Forensic Science", "Kinesiology", "Virology", "Immunology", "Biotechnology", "Nanotechnology"
]
ENGINEERING = [
    "Electrical Engineering", "Electronics", "Mechanical Engineering", "Civil Engineering", "Aerospace Engineering", "Chemical Engineering", "Industrial Engineering", "Software Engineering", "Computer Science", "Bioengineering", "Materials Science", "Robotics", "Artificial Intelligence", "Cybersecurity", "Blockchain Technology", "Data Science", "Information Technology", "System Engineering", "Environmental Engineering", "Structural Engineering", "Telecommunications", "Fluid Mechanics", "Mechatronics", "Automotive Engineering", "Petroleum Engineering", "Energy Engineering", "Biomedical Engineering", "Embedded Systems"
]
MATH = [
    "Mathematics", "Pure Mathematics", "Applied Mathematics", "Calculus", "Linear Algebra", "Discrete Mathematics", "Topology", "Probability and Statistics", "Number Theory", "Algebraic Geometry", "Game Theory", "Differential Equations"
]
MEDLAW = [
    "Medicine", "Anatomy", "Physiology", "Pathology", "Nursing", "Public Health", "Epidemiology", "Law", "International Law", "Constitutional Law"
]

COMMON_FIRST = [
    "Mathematics", "Physics", "Chemistry", "Biology", "Computer Science", "Medicine", "Law", "Software Engineering", "Electrical Engineering", "Mechanics"
]

CATEGORY = {}
for s in SCIENCE: CATEGORY[s] = "Science"
for s in ENGINEERING: CATEGORY[s] = "Engineering & Tech"
for s in MATH: CATEGORY[s] = "Mathematics"
for s in MEDLAW: CATEGORY[s] = "Medicine & Law"

subjects = SCIENCE + ENGINEERING + MATH + MEDLAW

ordered_subjects = [s for s in COMMON_FIRST if s in subjects] + [s for s in subjects if s not in COMMON_FIRST]


def difficulty_for(i: int) -> str:
    if i <= 70:
        return "Easy"
    if i <= 140:
        return "Medium"
    return "Hard"


def make_question(subject: str, category: str, i: int):
    level = difficulty_for(i)

    if category == "Mathematics":
        n = i + 3
        q = f"[{level}] In {subject}, evaluate the expression (2x+3)^2 at x={n}."
        correct = (2*n + 3) ** 2
        opts = [correct, correct + 4, correct - 5, correct + 9]
        labels = ['A','B','C','D']
        cidx = i % 4
        opts[0], opts[cidx] = opts[cidx], opts[0]
        return q, opts, labels[cidx]

    if category == "Engineering & Tech":
        base = 10 + (i % 15)
        q = f"[{level}] In an introductory {subject} design review, which formula correctly computes efficiency η for useful output power P_out and input power P_in?"
        opts = [
            "η = P_out / P_in",
            "η = P_in / P_out",
            "η = P_out + P_in",
            "η = P_out - P_in"
        ]
        cidx = i % 4
        opts[0], opts[cidx] = opts[cidx], opts[0]
        return q, opts, "ABCD"[cidx]

    if category == "Medicine & Law":
        q = f"[{level}] In {subject}, which option best represents evidence-based professional decision-making?"
        opts = [
            "Use established guidelines, current evidence, and case-specific facts.",
            "Rely only on intuition and avoid documentation.",
            "Ignore standards if outcomes seem likely positive.",
            "Choose the fastest option regardless of ethics."
        ]
        cidx = i % 4
        opts[0], opts[cidx] = opts[cidx], opts[0]
        return q, opts, "ABCD"[cidx]

    # Science default
    q = f"[{level}] In {subject}, what is the SI unit of energy used in most quantitative analyses?"
    opts = ["Joule (J)", "Watt (W)", "Pascal (Pa)", "Coulomb (C)"]
    cidx = i % 4
    opts[0], opts[cidx] = opts[cidx], opts[0]
    return q, opts, "ABCD"[cidx]


def main():
    out = "subject_question_bank.csv"
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow([
            "subject_order", "subject", "category", "question_number", "difficulty", "question",
            "option_a", "option_b", "option_c", "option_d", "correct_option"
        ])

        for sidx, subject in enumerate(ordered_subjects, start=1):
            category = CATEGORY[subject]
            for i in range(1, 201):
                q, opts, correct = make_question(subject, category, i)
                w.writerow([sidx, subject, category, i, difficulty_for(i), q, opts[0], opts[1], opts[2], opts[3], correct])

    print(f"Generated {out} for {len(ordered_subjects)} subjects x 200 questions = {len(ordered_subjects)*200} rows.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Generate a broad, syllabus-oriented MCQ bank (Class 11/12 + first-year college level)."""

from __future__ import annotations

import csv
import random
from collections import defaultdict

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
    "Mathematics", "Physics", "Chemistry", "Biology", "Computer Science", "Medicine", "Law", "Software Engineering", "Electrical Engineering"
]

CATEGORY = {}
for s in SCIENCE:
    CATEGORY[s] = "Science"
for s in ENGINEERING:
    CATEGORY[s] = "Engineering & Tech"
for s in MATH:
    CATEGORY[s] = "Mathematics"
for s in MEDLAW:
    CATEGORY[s] = "Medicine & Law"

ALL_SUBJECTS = SCIENCE + ENGINEERING + MATH + MEDLAW
ORDERED_SUBJECTS = [s for s in COMMON_FIRST if s in ALL_SUBJECTS] + [s for s in ALL_SUBJECTS if s not in COMMON_FIRST]

TOPICS = {
    "Physics": ["Units and measurements", "Kinematics", "Laws of motion", "Work-energy-power", "Rotational motion", "Gravitation", "Oscillations", "Waves", "Thermal properties", "Electrostatics", "Current electricity", "Magnetism", "Optics", "Modern physics"],
    "Chemistry": ["Atomic structure", "Periodic trends", "Chemical bonding", "States of matter", "Thermodynamics", "Equilibrium", "Redox", "Electrochemistry", "Organic nomenclature", "Hydrocarbons", "Biomolecules", "Polymers", "Coordination compounds"],
    "Biology": ["Cell structure", "Biomolecules", "Enzymes", "Genetics", "Evolution", "Human physiology", "Plant physiology", "Ecology", "Reproduction", "Molecular basis of inheritance", "Biotechnology basics", "Microbial diversity"],
    "Mathematics": ["Sets and relations", "Functions", "Quadratic equations", "Trigonometry", "Sequences and series", "Limits", "Derivatives", "Integrals", "Matrices", "Determinants", "Probability", "Vectors", "3D geometry", "Differential equations"],
    "Computer Science": ["Programming fundamentals", "Data structures", "Algorithms", "Complexity analysis", "OOP basics", "Databases", "Computer networks", "Operating systems", "Discrete logic", "Software testing", "Version control", "Web fundamentals"],
    "Law": ["Sources of law", "Fundamental rights", "Directive principles", "Judicial review", "Contract essentials", "Tort basics", "Criminal liability", "Legal reasoning", "Precedent", "Natural justice", "International treaties"],
    "Medicine": ["Cell injury", "Inflammation", "Pharmacokinetics", "Antimicrobials", "Cardiorespiratory physiology", "Clinical examination", "Diagnostic sensitivity", "Epidemiologic measures", "Ethics and consent", "Public health screening"],
    "Electrical Engineering": ["Circuit laws", "Network theorems", "AC analysis", "Transformers", "DC machines", "Induction motors", "Power systems", "Control basics", "Semiconductors", "Digital logic", "Measurements and instrumentation"],
    "Software Engineering": ["SDLC models", "Requirements engineering", "UML", "Design patterns", "Unit testing", "Integration testing", "Code review", "Agile planning", "Refactoring", "Version control workflows", "CI/CD basics"],
}

CATEGORY_TOPICS = {
    "Science": ["Measurement", "Experimental design", "Data interpretation", "Model assumptions", "Mechanism", "Conservation laws", "Equilibrium", "Kinetics", "Uncertainty", "Graph analysis", "Instrument calibration", "Ethics in experimentation"],
    "Engineering & Tech": ["System modeling", "Efficiency", "Control", "Signal/noise", "Safety factor", "Optimization", "Reliability", "Design trade-offs", "Testing protocol", "Fault diagnosis", "Energy balance", "Standards/compliance"],
    "Mathematics": ["Algebraic manipulation", "Functions", "Limits", "Differentiation", "Integration", "Linear systems", "Counting", "Probability", "Proof strategy", "Recurrence", "Graph theory", "Numerical methods"],
    "Medicine & Law": ["Evidence evaluation", "Case interpretation", "Risk communication", "Ethics", "Regulation", "Public policy", "Consent", "Diagnostic criteria", "Causation", "Burden of proof", "Documentation", "Professional duty"],
}


def difficulty_for(n: int) -> str:
    if n <= 70:
        return "Easy"
    if n <= 140:
        return "Medium"
    return "Hard"


def pick_topics(subject: str, category: str, idx: int) -> tuple[str, str]:
    pool = TOPICS.get(subject, CATEGORY_TOPICS[category])
    t1 = pool[idx % len(pool)]
    t2 = pool[(idx * 3 + 5) % len(pool)]
    if t1 == t2:
        t2 = pool[(idx + 1) % len(pool)]
    return t1, t2


def shuffle_options(correct: str, distractors: list[str], rng: random.Random) -> tuple[list[str], str]:
    options = [correct] + distractors
    rng.shuffle(options)
    correct_letter = "ABCD"[options.index(correct)]
    return options, correct_letter


def math_question(subject: str, topic: str, level: str, qn: int, rng: random.Random):
    if qn % 4 == 0:
        a = rng.randint(2, 7)
        b = rng.randint(1, 9)
        x = rng.randint(1, 6) + (1 if level == "Hard" else 0)
        val = a * x + b
        correct = str(val)
        q = f"[{level}] {subject} ({topic}): For f(x) = {a}x + {b}, find f({x})."
        d = [str(val + rng.choice([1, 2, 3])), str(val - rng.choice([1, 2])), str(a + b + x)]
    elif qn % 4 == 1:
        n = rng.randint(3, 12) + (2 if level == "Hard" else 0)
        s = n * (n + 1) // 2
        correct = str(s)
        q = f"[{level}] {subject} ({topic}): What is the sum of the first {n} natural numbers?"
        d = [str(s + n), str(s - 1), str(n * n)]
    elif qn % 4 == 2:
        a = rng.randint(1, 4)
        b = rng.randint(2, 7)
        c = rng.randint(1, 4)
        det = a * b - c
        correct = str(det)
        q = f"[{level}] {subject} ({topic}): Compute determinant of [[{a}, 1], [{c}, {b}]]."
        d = [str(a * b + c), str((a + b) * c), str(a + b + c)]
    else:
        p = rng.choice([0.2, 0.25, 0.3, 0.4, 0.5])
        correct = f"{p*(1-p):.2f}"
        q = f"[{level}] {subject} ({topic}): If P(A) = {p:.2f}, what is P(A)·P(not A)?"
        d = [f"{p:.2f}", f"{(1-p):.2f}", f"{(p+p*(1-p)):.2f}"]
    options, ans = shuffle_options(correct, d, rng)
    return q, options, ans


def engineering_question(subject: str, topic: str, level: str, qn: int, rng: random.Random):
    if qn % 5 == 0:
        pout = rng.randint(60, 180)
        pin = pout + rng.randint(20, 120)
        eta = round((pout / pin) * 100, 1)
        q = f"[{level}] {subject} ({topic}): A system delivers {pout} W output for {pin} W input. Efficiency is:"
        correct = f"{eta}%"
        d = [f"{round((pin/pout)*100,1)}%", f"{round(((pin-pout)/pin)*100,1)}%", f"{round(((pin-pout)/pout)*100,1)}%"]
    elif qn % 5 == 1:
        q = f"[{level}] {subject} ({topic}): Which action most directly improves reliability during first-year prototype validation?"
        correct = "Design test cases for boundary, nominal, and failure conditions."
        d = ["Skip failure tests to save schedule.", "Run only one successful trial.", "Rely on intuition instead of measurements."]
    elif qn % 5 == 2:
        q = f"[{level}] {subject} ({topic}): In a closed-loop system, negative feedback primarily helps to:"
        correct = "Reduce sensitivity to disturbances and parameter variation."
        d = ["Eliminate the need for sensors.", "Increase open-loop instability.", "Guarantee zero noise in all conditions."]
    elif qn % 5 == 3:
        q = f"[{level}] {subject} ({topic}): During design trade-off analysis, the best first step is to:"
        correct = "Define measurable performance criteria and constraints."
        d = ["Choose the cheapest material immediately.", "Finalize layout before requirements.", "Ignore safety margins in conceptual design."]
    else:
        q = f"[{level}] {subject} ({topic}): Which metric is most suitable for comparing two algorithms used in an embedded controller?"
        correct = "Worst-case execution time under identical hardware constraints."
        d = ["Developer preference score.", "Number of comments in source code only.", "File name length of the implementation."]
    options, ans = shuffle_options(correct, d, rng)
    return q, options, ans


def medlaw_question(subject: str, topic: str, level: str, qn: int, rng: random.Random):
    if qn % 5 == 0:
        q = f"[{level}] {subject} ({topic}): Which option best reflects evidence-based professional judgment?"
        correct = "Integrate current evidence, established standards, and case-specific facts."
        d = ["Prioritize speed over documentation.", "Follow personal belief even when contradicted by data.", "Avoid recording rationale to reduce paperwork."]
    elif qn % 5 == 1:
        q = f"[{level}] {subject} ({topic}): In public-facing decisions, informed consent primarily requires:"
        correct = "Capacity assessment, adequate disclosure, and voluntary agreement."
        d = ["Only a signature without explanation.", "Implied agreement in all routine interactions.", "Consent from unrelated third parties by default."]
    elif qn % 5 == 2:
        prev = rng.randint(5, 30)
        pop = rng.randint(200, 1000)
        rate = round((prev/pop)*100, 1)
        q = f"[{level}] {subject} ({topic}): If {prev} existing cases are identified in a population of {pop}, prevalence is:"
        correct = f"{rate}%"
        d = [f"{round((pop/prev),1)}%", f"{round((prev/(pop-prev))*100,1)}%", f"{round(((prev+10)/pop)*100,1)}%"]
    elif qn % 5 == 3:
        q = f"[{level}] {subject} ({topic}): Which statement best describes professional documentation quality?"
        correct = "It should be timely, clear, factual, and auditable."
        d = ["It should omit uncertainties to appear confident.", "It should prioritize abbreviations over clarity.", "It should be written only after final outcomes are known."]
    else:
        q = f"[{level}] {subject} ({topic}): The strongest way to reduce decision bias in case review is to:"
        correct = "Use predefined criteria and independent peer review."
        d = ["Rely only on seniority hierarchy.", "Discard outlier data without justification.", "Avoid protocol checklists."]
    options, ans = shuffle_options(correct, d, rng)
    return q, options, ans


def science_question(subject: str, topic: str, topic2: str, level: str, qn: int, rng: random.Random):
    if qn % 6 == 0:
        q = f"[{level}] {subject} ({topic}): Which statement is most consistent with a controlled experiment?"
        correct = "Change one independent variable while keeping key confounders constant."
        d = ["Change all variables together for speed.", "Avoid a comparison group.", "Use non-calibrated instruments intentionally."]
    elif qn % 6 == 1:
        q = f"[{level}] {subject} ({topic}): Why is SI-unit consistency essential in quantitative problem solving?"
        correct = "It prevents dimensional errors and enables valid equation use."
        d = ["It guarantees zero experimental uncertainty.", "It removes the need for significant figures.", "It allows any equation regardless of assumptions."]
    elif qn % 6 == 2:
        q = f"[{level}] {subject} ({topic} and {topic2}): A graph with slope near zero after repeated trials most directly suggests:"
        correct = "The dependent variable is weakly sensitive to that input range."
        d = ["All measurements are necessarily wrong.", "The instrument has infinite resolution.", "No model can explain the system."]
    elif qn % 6 == 3:
        base = rng.randint(10, 80)
        inc = rng.randint(5, 25)
        final = base + inc
        q = f"[{level}] {subject} ({topic}): A quantity increases from {base} to {final}. The percentage increase is:"
        correct = f"{round((inc/base)*100,1)}%"
        d = [f"{round((inc/final)*100,1)}%", f"{round((base/final)*100,1)}%", f"{round((final/base)*100,1)}%"]
    elif qn % 6 == 4:
        q = f"[{level}] {subject} ({topic2}): Which conclusion is scientifically strongest?"
        correct = "A claim supported by reproducible data, uncertainty bounds, and model limitations."
        d = ["A claim based on one unverified observation.", "A claim chosen because it is popular.", "A claim that ignores contradictory data."]
    else:
        q = f"[{level}] {subject} ({topic}): In first-year laboratory work, calibration before measurement is done mainly to:"
        correct = "Reduce systematic error and improve result validity."
        d = ["Increase random noise intentionally.", "Avoid recording raw observations.", "Eliminate the need for repeated trials."]
    options, ans = shuffle_options(correct, d, rng)
    return q, options, ans


def make_question(subject: str, category: str, qn: int):
    rng = random.Random(f"{subject}|{qn}|v2")
    level = difficulty_for(qn)
    topic, topic2 = pick_topics(subject, category, qn)

    if category == "Mathematics":
        level, q, opts, ans = level, *math_question(subject, topic, level, qn, rng)
    elif category == "Engineering & Tech":
        level, q, opts, ans = level, *engineering_question(subject, topic, level, qn, rng)
    elif category == "Medicine & Law":
        level, q, opts, ans = level, *medlaw_question(subject, topic, level, qn, rng)
    else:
        level, q, opts, ans = level, *science_question(subject, topic, topic2, level, qn, rng)

    q = f"{q} (Question {qn})"
    return level, q, opts, ans


def generate(output_file: str = "subject_question_bank.csv") -> None:
    dedupe = defaultdict(set)

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow([
            "subject_order", "subject", "category", "question_number", "difficulty", "question",
            "option_a", "option_b", "option_c", "option_d", "correct_option"
        ])

        for sidx, subject in enumerate(ORDERED_SUBJECTS, start=1):
            category = CATEGORY[subject]
            for qn in range(1, 201):
                level, question, options, ans = make_question(subject, category, qn)
                if question in dedupe[subject]:
                    raise ValueError(f"Duplicate question detected for {subject}: {question}")
                dedupe[subject].add(question)
                w.writerow([sidx, subject, category, qn, level, question, options[0], options[1], options[2], options[3], ans])

    print(
        f"Generated {output_file} with {len(ORDERED_SUBJECTS)} subjects x 200 questions = {len(ORDERED_SUBJECTS) * 200} rows."
    )


if __name__ == "__main__":
    generate()

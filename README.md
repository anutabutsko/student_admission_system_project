# Max Heap-based Student Admission System

This repository contains a Python script for a simple student admissions system. The system processes student applications, prioritizes them based on certain criteria, and makes admission offers to the most qualified candidates. Additionally, it simulates a random dataset of student applications for testing purposes.

## Table of Contents
- [Dependencies](#dependencies)
- [Max Heap Implementation](#max-heap-implementation)
- [Student Data Structure](#student-data-structure)
- [Admission Priority](#admission-priority)
- [Processing Admissions](#processing-admissions)
- [Making Admission Offers](#making-admission-offers)
- [Random Student Dataset](#random-student-dataset)
- [Usage](#usage)

## Dependencies <a name="dependencies"></a>

Before running the script, ensure you have requirements.txt installed:
```bash
pip install -r requirements.txt
```

## Max Heap Implementation <a name="max-heap-implementation"></a>

The script includes a max heap implementation for efficiently prioritizing student admission requests. It is used to maintain a heap of students with the highest priority at the top.

## Student Data Structure <a name="student-data-structure"></a>

Student data is represented as a dictionary containing the following fields:
- `name`: Student's name
- `student_type`: Student type (e.g., Undergraduate, Graduate, Auditor)
- `computer_science`: Boolean indicating if the student has a computer science background
- `math`: Boolean indicating if the student has a math background
- `year`: Student's current academic year
- `orientation_day`: The day the student registered for orientation
- `email`: Student's email address
- `address`: Student's address (generated using Faker)

## Admission Priority <a name="admission-priority"></a>

The `priority` function calculates a priority score for each student based on the following criteria:
- Graduate students have a higher priority.
- Computer Science students are preferred.
- Math students are given preference.
- Students closer to graduation are prioritized.
- Earlier registration dates (orientation days) get higher preference.
- In the event of a tie, the original index is used as a unique identifier.

## Processing Admissions <a name="processing-admissions"></a>

The `process_admissions` function processes student admission requests, prioritizes them, and admits up to 25 students based on their priority scores. Admitted students are stored in a list.

## Making Admission Offers <a name="making-admission-offers"></a>

The `make_offers` function makes admission offers to admitted students. It checks for students who have not dropped the class and offers admission to them. If there are empty spots, it fills them with the most qualified students from the remaining applicants.

## Random Student Dataset <a name="random-student-dataset"></a>

The script includes a `random_student_admission` function that generates a random dataset of student applications for testing purposes. It uses the Faker library to create realistic student data.

## Usage <a name="usage"></a>

1. Ensure you have installed the required dependencies as mentioned in the [Dependencies](#dependencies) section.

2. You can modify the script to change the number of randomly generated student applications by modifying the `random_student_admission` function's `size` parameter.

3. Run the script to simulate the admission process, prioritize students, and generate admission offers. The results are saved to a CSV file named `offers_data.csv`.

```bash
python heap_project.py
```

4. You can inspect the generated admission offers in the `offers_data.csv` file.

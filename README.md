# Max Heap-based Student Admission System

## Overview

This system implements a student admission process based on prioritized criteria using Max Heap. Students are processed based on factors like student type, academic achievements, registration date, etc., and offers are made to the top 25 applicants. The system also accommodates dropout scenarios and makes additional offers to fill vacancies.

## Features

- **Max Heap Implementation**: Functions `max_heap()` and `pop_max_heap()` offer insertion and extraction for max heap data structure respectively.

- **Student Data Organizer**: The `student_data()` function generates a structured dictionary for each student with their profile data.

- **Prioritization System**: The `priority()` function calculates priority for each student based on defined criteria.

- **Admission Processor**: `process_admissions()` reviews the student data and prioritizes each student for admissions.

- **Offer Generator**: The `make_offers()` function simulates the offer-making process, considering any dropouts, and fills in available spots with the next prioritized students.

## Sample Usage

The main script offers a demonstration with a mock dataset of students with superhero names. Based on the dataset, the top 25 students are admitted. Additionally, the system simulates the case where some students drop out and new offers are made to fill those spots.

To execute, simply run:

```python
print("Offers in order:")
for index, offer in enumerate(offers):
    print(index + 1, offer["name"])
```

## Prioritization Logic

The prioritization logic is applied as follows:

1. Graduate students have a higher priority.
2. Computer Science students are preferred.
3. Math students are given preference.
4. Students closer to graduation are prioritized.
5. Earlier registration dates (orientation days) get higher preference.
6. In the event of a tie, the original index is used as a unique identifier.
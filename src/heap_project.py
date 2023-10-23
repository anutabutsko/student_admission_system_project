# Import Libraries
import numpy as np
import pandas as pd
from faker import Faker


# Max heap implementation
def max_heap(lst, value):
    lst.append(value)  # Add the new value to the end of the heap
    idx = len(lst) - 1  # Get the index of the newly added element

    # Moving the newly added element up the tree as long as it's greater
    # than its parent, maintaining the max heap property
    while idx > 0:
        parent_index = (idx - 1) // 2
        if lst[idx] > lst[parent_index]:
            lst[idx], lst[parent_index] = lst[parent_index], lst[idx]
            idx = parent_index
        else:
            break


# Pop max heap implementation
def pop_max_heap(lst):
    # Checking if list is empty
    if not list:
        return "The array is empty"

    # Checking if there is only one element in the list
    if len(lst) == 1:
        return lst.pop()

    # Maximum element
    max_elem = lst[0]
    # Last element
    last = lst.pop()

    if lst:
        # Moving the last element to the root position
        lst[0] = last
        index = 0
        n = len(lst)

        # Restore the tree by bringing down the element
        while True:
            left = index * 2 + 1
            right = index * 2 + 2
            largest = index

            # Comparing the largest value to the left child
            if left < n and lst[largest] < lst[left]:
                largest = left

            # Comparing the largest value to the right child
            if right < n and lst[largest] < lst[right]:
                largest = right

            # Checking if largest index has been changed
            # No need to swap elements or call function recursively if largest element was not changed
            if largest != index:
                # Swapping the values of the parent with the largest element
                lst[largest], lst[index] = lst[index], lst[largest]
                index = largest
            else:
                break

    # Returning the maximum element that was removed
    return max_elem


# Function that organizes student payload into a dictionary
def student_data(name, student_type, computer_science, math, year, orientation_day, email, fake_address):
    return {"name": name,
            "student_type": student_type,
            "computer_science": computer_science,
            "math": math,
            "year": year,
            "orientation_day": orientation_day,
            "email": email,
            "address": fake_address}


# Prioritizing each student
def priority(payload, idx):
    lst_priority = [
        1 if payload["student_type"] == "Graduate" else 0,
        1 if payload["computer_science"] is True else 0,
        1 if payload["math"] is True else 0,
        payload["year"],  # Closer students are graduating - higher the priority
        -payload["orientation_day"],
        # Reversing the orientation day value to give priority to students that register earlier
        idx  # Unique identifier of each student
    ]

    return lst_priority


# Processing each student and admitting by priority criteria
def process_admissions(payload):
    lst = []
    admitted_students = []  # Initialize a list for admitted students

    # Enumerating through student requests and prioritizing them
    for idx, student in enumerate(payload):
        priority_student = priority(student, idx)
        max_heap(lst, priority_student)  # Adding every priority to our max heap

    # Admitting students up to a limit 25 based on max heap priorities
    while len(admitted_students) < 25 and len(lst) > 0:
        _, computer_science, math, year, orientation_day, idx = pop_max_heap(lst)
        admitted_students.append(idx)

    return admitted_students


# Making offers to admitted students if places become available
def make_offers(payload, admitted_students, dropouts):
    offers = []

    # Checking for admitted students who haven't dropped the class
    for idx, request in enumerate(payload):
        if idx in admitted_students and idx not in dropouts:
            offers.append(request)

    # Filling empty spots with the most qualified students
    while len(offers) < 25:
        # Checking for the next most qualified student who hasn't been previously admitted
        next_student = None
        for index, request in enumerate(payload):
            if index not in admitted_students and index not in dropouts:
                if next_student is None or priority(request, index) > priority(next_student, index):
                    next_student = request

        # If no more qualified students are available, break the loop
        if next_student is None:
            break

        # Marking the student as admitted and add them to the offers list
        admitted_students.append(payload.index(next_student))
        offers.append(next_student)

    return offers


# Make a random fake data set of size n
def random_student_admission(size=40):
    # Initialize Faker
    fake = Faker()

    # Create list of student_data dicts
    student_list = []
    for individual in range(0, size):
        name = fake.name()
        student_type = np.random.choice(['Undergraduate', 'Graduate', 'Auditor'])
        computer_science = np.random.choice([True, False])
        math = np.random.choice([True, False])
        year = np.random.randint(0, 5)
        orientation = np.random.randint(0, 6)
        fake_email = fake.free_email()
        fake_address = fake.address()
        student_list.append(student_data(name, student_type, computer_science, math, year, orientation, fake_email,fake_address))
        
    return student_list


# main script

# Creating sample payload
# data = [student_data("Spider-man", "Graduate", False, True, 2, 2),
#         student_data("Black Panther", "Undergraduate", True, True, 4, 1),
#         student_data("Deadpool", "Graduate", False, False, 3, 3),
#         student_data("Captain America", "Auditor", True, False, 0, 4),
#         student_data("Ironman", "Graduate", False, False, 2, 1),
#         student_data("Ant-man", "Undergraduate", False, True, 4, 5),
#         student_data("Captain Marvel", "Graduate", True, True, 1, 1),
#         student_data("Superman", "Auditor", True, False, 0, 5),
#         student_data("Batman", "Graduate", False, False, 4, 2),
#         student_data("Hulk", "Undergraduate", True, True, 4, 3),
#         student_data("Iceman", "Graduate", False, False, 1, 3),
#         student_data("Aquaman", "Auditor", True, True, 2, 4),
#         student_data("Thor", "Graduate", True, True, 3, 2),
#         student_data("Asterix", "Undergraduate", False, True, 2, 1),
#         student_data("Ghost Rider", "Graduate", False, False, 3, 1),
#         student_data("Hell-boy", "Auditor", True, False, 2, 4),
#         student_data("Robin", "Graduate", False, True, 4, 5),
#         student_data("The Rocketeer", "Undergraduate", False, True, 1, 5),
#         student_data("Watchmen", "Graduate", True, False, 1, 3),
#         student_data("Catwoman", "Auditor", True, False, 2, 5),
#         student_data("Flash", "Graduate", True, False, 0, 1),
#         student_data("Doctor Strange", "Undergraduate", True, True, 2, 3),
#         student_data("Daredevil", "Graduate", True, False, 3, 5),
#         student_data("Namor", "Auditor", False, False, 0, 4),
#         student_data("Vision", "Graduate", True, True, 0, 5),
#         student_data("Groot", "Auditor", True, True, 1, 5),
#         student_data("Wasp", "Graduate", True, False, 4, 2),
#         student_data("Nick Fury", "Undergraduate", False, True, 3, 2),
#         student_data("Nightcrawler", "Graduate", False, False, 1, 1),
#         student_data("Wonder Woman", "Auditor", False, True, 0, 1)]

# admitted_students = process_admissions(data)

# # print("Admitted students in order:")
# # for index, idx in enumerate(admitted_students):
# #     print(index+1, payload[idx]["name"])

# # Simulating dropouts
# dropouts = [admitted_students[3], admitted_students[17]]

# # Making offers if places become available
# offers = make_offers(data, admitted_students, dropouts)

# offer_df = pd.DataFrame(offers)

# print(f"Offers in order:\n {offer_df}")




rand_stud = random_student_admission(27)
admitted_students = process_admissions(rand_stud)
dropouts = [admitted_students[3], admitted_students[17]]
offers = make_offers(rand_stud, admitted_students, dropouts)
offer_df = pd.DataFrame(offers)
print(f"Offers in order:\n {offer_df}")

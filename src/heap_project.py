# Import Libraries
import numpy as np
import pandas as pd
from faker import Faker


# Max Heap Implementation
def max_heap(lst, n, i):
    largest = i
    # Calculating positions of left and right children
    left = i * 2 + 1
    right = i * 2 + 2

    # Comparing the largest value to the left child
    if left < n and lst[largest] < lst[left]:
        largest = left

    # Comparing the largest value to the right child
    if right < n and lst[largest] < lst[right]:
        largest = right

    # Checking if largest index has been changed
    # No need to swap elements or call function recursively if largest element was not changed
    if largest != i:
        # Swapping the values of the parent with the largest element
        lst[largest], lst[i] = lst[i], lst[largest]

        # Call function recursively to check children values
        max_heap(lst, n, largest)


# Add a new value to the heap
def add_heap(lst, value):
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


# Pop max element from heap
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
        max_heap(lst, index, n)

    # Returning the maximum element that was removed
    return max_elem


# Prioritizing each student
def priority(payload, idx):
    lst_priority = [
        1 if payload["student_type"] == "Graduate" else 0,
        1 if payload["computer_science"] is True else 0,
        1 if payload["math"] is True else 0,
        payload["year"],  # Closer students are graduating - higher the priority
        -payload["orientation_day"],  # Reversing the orientation day value to give priority to students that register earlier
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
        add_heap(lst, priority_student)  # Adding every priority to our max heap

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


# Function that organizes student payload into a dictionary
def student_data(name, student_type, computer_science, math, year, orientation_day, email, street, city, state, zip_code):
    return {"name": name,
            "student_type": student_type,
            "computer_science": computer_science,
            "math": math,
            "year": year,
            "orientation_day": orientation_day,
            "email": email,
            "Street Address": street,
            "City": city,
            "State": state,
            "ZIP Code": zip_code}


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
        orientation = np.random.randint(1, 6)
        fake_email = fake.free_email()
        fake_address = fake.street_address()
        fake_city = fake.city()
        fake_state = fake.state()
        fake_zip = fake.postcode()
        student_list.append(
            student_data(name, student_type, computer_science, math, year, orientation, fake_email, fake_address, fake_city, fake_state, fake_zip))

    return student_list


# Create Random Student List
rand_stud = random_student_admission(27)
rand_stud_df = pd.DataFrame(rand_stud)

# Process Student admissions with 2 dropouts
admitted_students = process_admissions(rand_stud)
dropouts = [admitted_students[3], admitted_students[17]]
# Make Offers
offers = make_offers(rand_stud, admitted_students, dropouts)
offers_df = pd.DataFrame(offers)
print(f"Offers in order:\n {offers_df}")

offers_df.to_csv('offers_data.csv')

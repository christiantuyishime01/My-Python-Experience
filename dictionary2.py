#!/bin/usr/env python3
student_profile = {
    "names": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "grades": [8, 9, 7, 8, 2]
}
# Data extraction and display
# 1. Print all different values present in key 1 (names)
print("All student names:")
for name in set(student_profile["names"]):
    print(name)

# 2. Print all values present in key 2 (grades)
print("\nALL student grades:")
for grade in student_profile["grades"]:
    print(grade)

# 3. Print a message with the following structure "Student (name) obtained (grade)% in BSE. "
print("\nStudent grades:")
for name, grade in zip(student_profile["names"], student_profile["grades"]):
    print(f"Student {name} obtained {grade}% in BSE.")
    
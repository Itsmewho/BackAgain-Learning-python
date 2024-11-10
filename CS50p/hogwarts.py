# List and dicts are up.

# students = ["Ron", "Hermelien", "Harry", "Draco"]

# for items in range(len(students)):
#     print(items + 1, students[items])


students = {
    "Hermelien": "Griffendor",
    "Harry": "Griffendor",
    "Ron": "Griffendor",
    "Draco": "Slytherin",
}

print(students["Ron"])

# For this last one you have to understand that the students in the list are the key's and the student the value. C below.

for student in students:  # student is the item students is the dict it self.
    print(
        student, students[student], sep=", "
    )  # same here but now you have first the item. than the list. from this list you want the student + value. the for loop will do the rest.

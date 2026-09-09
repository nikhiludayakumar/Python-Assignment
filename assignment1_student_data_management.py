"""
# Name       : Nikhil Udayakumar
# PRN        : 1272261861
# Division   : 9
# Branch     : CSE (AI-DS)
# Subject    : Python 
# Batch      : 1
Assignment 1
Problem Statement: Student Data Management Using Python Collections
"""

def display_students(students):
    """Display all student records stored in the dictionary."""
    print("\n--- Student Records ---")
    if not students:
        print("No records found.")
        return
    for roll_no, details in students.items():
        # details is stored as a tuple: (Name, Branch, Marks)
        name, branch, marks = details
        print(f"Roll No: {roll_no} | Name: {name} | Branch: {branch} | Marks: {marks}")
    print("------------------------\n")


def add_student(students, roll_no, name, branch, marks):
    """Add a new student record to the dictionary using a tuple as the value."""
    if roll_no in students:
        print(f"Student with Roll No {roll_no} already exists. Use update instead.")
    else:
        students[roll_no] = (name, branch, marks)  # Tuple: immutable record
        print(f"Added student with Roll No {roll_no}.")


def delete_student(students, roll_no):
    """Delete an existing student record from the dictionary."""
    if roll_no in students:
        del students[roll_no]
        print(f"Deleted student with Roll No {roll_no}.")
    else:
        print(f"Student with Roll No {roll_no} not found.")


def update_student(students, roll_no, name=None, branch=None, marks=None):
    """Update details of an existing student. Only provided fields are changed."""
    if roll_no not in students:
        print(f"Student with Roll No {roll_no} not found.")
        return

    old_name, old_branch, old_marks = students[roll_no]
    new_name = name if name is not None else old_name
    new_branch = branch if branch is not None else old_branch
    new_marks = marks if marks is not None else old_marks

    students[roll_no] = (new_name, new_branch, new_marks)
    print(f"Updated student with Roll No {roll_no}.")


def main():
    # Dictionary to hold all student records: key = Roll Number, value = Tuple(Name, Branch, Marks)
    students = {}

    # List used to keep track of roll numbers in the order they were added
    roll_number_list = []

    # Add new student records
    add_student(students, 101, "Nikhil", "Computer Engineering", 88)
    roll_number_list.append(101)

    add_student(students, 102, "Aditi", "Information Technology", 92)
    roll_number_list.append(102)

    add_student(students, 103, "Rohan", "Electronics", 75)
    roll_number_list.append(103)

    display_students(students)

    # Update an existing student's details
    update_student(students, 102, marks=95)

    # Delete an existing student record
    delete_student(students, 103)
    roll_number_list.remove(103)

    # Display final student records
    display_students(students)

    print("Roll numbers currently tracked (List):", roll_number_list)


if __name__ == "__main__":
    main()

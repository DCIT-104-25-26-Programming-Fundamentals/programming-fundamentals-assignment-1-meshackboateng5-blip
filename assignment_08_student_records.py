# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
students = []


def show_menu():
    print("=" * 36)
    print("    STUDENT RECORD SYSTEM MENU")
    print("=" * 36)
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def add_student():
    name = input("Student name: ")
    id_input = input("Student ID: ")
    if not id_input.isdigit():
        print("Error: Student ID must be a number.")
        return
    student_id = int(id_input)

    count_input = input("How many scores? ")
    if not count_input.isdigit() or int(count_input) <= 0:
        print("Error: Please enter a valid positive number of scores.")
        return
    count = int(count_input)

    scores = []
    for i in range(1, count + 1):
        score_input = input(f"Enter score {i}: ")
        try:
            scores.append(float(score_input))
        except ValueError:
            print("Error: Scores must be numbers.")
            return

    students.append({"name": name, "id": student_id, "scores": scores})
    print(f'Student "{name}" added successfully.')


def display_students():
    if not students:
        print("No students have been added yet.")
        return

    print("-" * 55)
    print(f"{'Name':<20}{'ID':<15}{'Scores':<15}{'Average':<10}")
    print("-" * 55)
    for s in students:
        avg = round(sum(s["scores"]) / len(s["scores"]), 2)
        scores_str = ", ".join(str(sc) for sc in s["scores"])
        print(f"{s['name']:<20}{s['id']:<15}{scores_str:<15}{avg:<10}")
    print("-" * 55)


def calculate_average():
    id_input = input("Enter student ID: ")
    if not id_input.isdigit():
        print("Error: Please enter a valid student ID.")
        return
    student_id = int(id_input)

    for s in students:
        if s["id"] == student_id:
            avg = round(sum(s["scores"]) / len(s["scores"]), 2)
            print(f"{s['name']}'s average score: {avg}")
            return

    print(f"Error: No student found with ID {student_id}.")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            calculate_average()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Please enter a number between 1 and 4.")

        print()


if __name__ == "__main__":
    main()
# =============================================================================


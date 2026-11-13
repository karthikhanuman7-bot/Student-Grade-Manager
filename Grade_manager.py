
# STUDENT GRADE MANAGER

students = []


# Function to calculate grade
def calculate_grade(mark):
    if 90 <= mark <= 100:
        return "A"
    elif 80 <= mark <= 89:
        return "B"
    elif 70 <= mark <= 79:
        return "C"
    elif 60 <= mark <= 69:
        return "D"
    else:
        return "E"


# Function to add student details
def add_student():

    name = input("Enter student name: ").strip()

    if not name:
        print("Invalid Input")
        return

    mark_input = input("Enter student mark (0-100): ")

    try:
        mark = int(mark_input)

        if mark < 0 or mark > 100:
            print("Invalid Input")
            return

        grade = calculate_grade(mark)

        students.append({
            "name": name,
            "mark": mark,
            "grade": grade
        })

        print("Student added successfully!")

    except ValueError:
        print("Invalid Input")


# Function to display final report
def display_report():

    if not students:
        print("No student records found.")
        return

    # Display student details in table
    print("\n")
    print("=" * 55)
    print("              STUDENT GRADE REPORT")
    print("=" * 55)

    print("{:<20} {:<15} {:<10}".format(
        "Student Name", "Mark", "Grade"
    ))

    print("-" * 55)

    for student in students:
        print("{:<20} {:<15} {:<10}".format(
            student["name"],
            student["mark"],
            student["grade"]
        ))

    print("=" * 55)

    # Calculate class statistics
    marks = [student["mark"] for student in students]

    average = sum(marks) / len(marks)

    highest = max(students, key=lambda s: s["mark"])
    lowest = min(students, key=lambda s: s["mark"])

    # Display statistics outside the table
    print("\n          CLASS PERFORMANCE SUMMARY")
    print("-" * 45)

    print("Total Number of Students :", len(students))
    print("Class Average            : {:.2f}".format(average))
    print("Highest Mark             :", highest["mark"])
    print("Highest Scorer           :", highest["name"])
    print("Lowest Mark              :", lowest["mark"])
    print("Lowest Scorer            :", lowest["name"])

    print("-" * 45)


# Main menu
def main():

    while True:

        print("\n===== STUDENT GRADE MANAGER =====")
        print("1. Add Student")
        print("2. Display Final Report")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_report()

        elif choice == "3":
            print("Thank you for using Student Grade Manager!")
            break

        else:
            print("Invalid Input")


# Start program
if __name__ == "__main__":
    main()


# ==========================================
#       STUDENT GRADE MANAGER
# ==========================================

# List to store student records

students = []


# ------------------------------------------
# 1. FUNCTION TO CALCULATE GRADE
# ------------------------------------------

def calculate_grade(marks):

    if marks >= 90:
        return "A+", "Outstanding! Excellent performance."

    elif marks >= 80:
        return "A", "Excellent work! Keep it up."

    elif marks >= 70:
        return "B+", "Very good! You're doing well."

    elif marks >= 60:
        return "B", "Good work! Keep improving."

    elif marks >= 50:
        return "C", "Satisfactory. You can do better."

    elif marks >= 40:
        return "D", "Need improvement. Focus more."

    else:
        return "E", "Needs serious improvement."


# ------------------------------------------
# 2. FUNCTION TO CHECK PASS OR FAIL
# ------------------------------------------

def check_result(marks):

    if marks >= 40:
        return "PASS"

    else:
        return "FAIL"


# ------------------------------------------
# 3. FUNCTION TO ADD STUDENT
# ------------------------------------------

def add_student():

    print("\n========== ADD STUDENT ==========")

    try:

        name = input("Enter student name: ").strip()

        # Validate student name

        if not name:
            print("Error: Student name cannot be empty.")
            return

        if not name.replace(" ", "").isalpha():
            print("Error: Please enter a valid name.")
            return

        # Get student marks

        marks = float(input("Enter student marks (0-100): "))

        # Validate marks

        if marks < 0 or marks > 100:
            print("Error: Marks must be between 0 and 100.")
            return

        # Calculate grade and feedback

        grade, feedback = calculate_grade(marks)

        # Determine pass or fail

        result = check_result(marks)

        # Store student information

        student = {
            "name": name,
            "marks": marks,
            "grade": grade,
            "feedback": feedback,
            "result": result
        }

        students.append(student)

        # Display individual student report

        print("\n========== STUDENT REPORT ==========")

        print(f"Student Name : {name}")
        print(f"Student Marks: {marks:g}")
        print(f"Student Grade: {grade}")
        print(f"Result       : {result}")
        print(f"Feedback     : {feedback}")

        print("====================================")

        print("\nStudent added successfully!")

    except ValueError:
        print("Invalid input! Please enter numeric marks.")

    except Exception as error:
        print(f"Unexpected error: {error}")


# ------------------------------------------
# 4. FUNCTION TO DISPLAY ALL STUDENTS
# ------------------------------------------

def display_students():

    if not students:
        print("\nNo student records found.")
        return

    print("\n")
    print("=" * 75)
    print("                 STUDENT GRADE REPORT")
    print("=" * 75)

    print("{:<20} {:<12} {:<10} {:<10}".format(
        "Student Name", "Marks", "Grade", "Result"
    ))

    print("-" * 75)

    for student in students:

        print("{:<20} {:<12} {:<10} {:<10}".format(
            student["name"],
            student["marks"],
            student["grade"],
            student["result"]
        ))

    print("=" * 75)


# ------------------------------------------
# 5. FUNCTION TO CALCULATE CLASS AVERAGE
# ------------------------------------------

def calculate_average():

    if not students:
        print("\nNo student records available.")
        return

    # Extract marks using list comprehension

    marks = [student["marks"] for student in students]

    # Calculate average

    average = sum(marks) / len(marks)

    print("\n========== CLASS AVERAGE ==========")

    print(f"Total Students: {len(students)}")
    print(f"Total Marks   : {sum(marks):g}")
    print(f"Class Average : {average:.2f}")

    print("===================================")


# ------------------------------------------
# 6. FUNCTION TO DISPLAY CLASS STATISTICS
# ------------------------------------------

def display_statistics():

    if not students:
        print("\nNo student records available.")
        return

    # Calculate highest and lowest scorers

    highest = max(students, key=lambda s: s["marks"])

    lowest = min(students, key=lambda s: s["marks"])

    # Count pass and fail students

    passed = 0
    failed = 0

    for student in students:

        if student["result"] == "PASS":
            passed += 1

        else:
            failed += 1

    # Calculate pass percentage

    pass_percentage = (passed / len(students)) * 100

    print("\n========== CLASS STATISTICS ==========")

    print(f"Total Students : {len(students)}")
    print(f"Passed Students: {passed}")
    print(f"Failed Students: {failed}")

    print(f"Pass Percentage: {pass_percentage:.2f}%")

    print("\n--- TOP PERFORMANCE ---")

    print(f"Highest Scorer: {highest['name']}")
    print(f"Highest Marks : {highest['marks']:g}")

    print("\n--- LOWEST PERFORMANCE ---")

    print(f"Lowest Scorer: {lowest['name']}")
    print(f"Lowest Marks : {lowest['marks']:g}")

    print("=======================================")


# ------------------------------------------
# 7. MAIN MENU FUNCTION
# ------------------------------------------

def main():

    while True:

        print("\n")
        print("====================================")
        print("       STUDENT GRADE MANAGER")
        print("====================================")

        print("1. Add Student")
        print("2. Display All Students")
        print("3. Calculate Class Average")
        print("4. Display Class Statistics")
        print("5. Exit")

        print("====================================")

        try:

            choice = int(input("Enter your choice (1-5): "))

            if choice == 1:

                add_student()

            elif choice == 2:

                display_students()

            elif choice == 3:

                calculate_average()

            elif choice == 4:

                display_statistics()

            elif choice == 5:

                print("\nThank you for using Student Grade Manager!")

                print("Have a great day!")

                break

            else:

                print("\nInvalid choice! Please select between 1 and 5.")

        except ValueError:

            print("\nInvalid input! Please enter a number between 1 and 5.")

        except Exception as error:

            print(f"\nUnexpected error: {error}")


# ------------------------------------------
# 8. PROGRAM EXECUTION
# ------------------------------------------

if __name__ == "__main__":

    main()

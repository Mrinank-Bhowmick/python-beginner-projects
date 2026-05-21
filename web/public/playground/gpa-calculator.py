# === GPA Calculator · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @nilay-banerjee.

import math


# Compute GPA from course marks and credits
def calculate_gpa(num_courses, marks):
    # Start credit accumulators at zero
    credits = 0
    total_credits = 0

    # Collect details for each course
    for i in range(num_courses):
        # Ask for course name and its credit value
        course_name = input("Enter Course Name: ")
        course_credits = int(input(f"Enter Total Credits Of {course_name}: "))

        # Either enter total marks or split marks
        if marks == 0:
            course_marks = int(input(f"Enter Total Marks Acquired for {course_name}: "))
        else:
            mid_sem_marks = int(input(f"Enter Your Mid Sem Marks for {course_name}: "))
            internal_marks = int(
                input(f"Enter Your Internal Marks for {course_name}: ")
            )
            end_sem_marks = int(input(f"Enter Your End Sem Marks for {course_name}: "))
            course_marks = mid_sem_marks + internal_marks + end_sem_marks

        print()

        # Validate marks are within 0–100 range
        if course_marks > 100:
            print("Enter Valid Marks")
            credits = 0
            total_credits = 1
            break
        elif course_marks < 100:
            course_marks += 1

        # Convert marks to grade points using ceiling
        course_point = math.ceil(course_marks / 10)

        # Add weighted points to running totals
        credits += course_point * course_credits
        total_credits += course_credits

    # Divide total weighted points by total credits
    gpa = credits / total_credits
    return gpa


if __name__ == "__main__":
    print("\n------------------------------------------")
    print("GPA Calculator: ")
    print("------------------------------------------")

    # Get number of courses and mark-entry preference
    num_courses = int(input("Enter Number Of Courses: "))
    marks = int(
        input(
            "Enter 1 to individually enter Mid Sem, Internals & End Sem Marks\nElse Enter 0 to enter Total Marks: "
        )
    )

    # Calculate and print the semester GPA
    gpa = calculate_gpa(num_courses, marks)
    print("Your Credits for this Semester is:", gpa)

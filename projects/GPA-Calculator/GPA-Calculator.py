import math

print("\n------------------------------------------")
print("GPA Calculator: ")
print("------------------------------------------")

n = int(input("Enter Number Of Courses: "))
midSem = int(
    input(
        "Enter 1 to individually enter Mid Sem, Internals & End Sem Marks\nElse Enter 0 to enter Total Marks: "
    )
)

Credits = 0
totalCredits = 0

for i in range(n):
    course_name = input("Enter Course Name: ")
    course_Credits = int(input(f"Enter Total Credits Of {course_name}: "))
    
    try:
        if midSem == 0:
            course_Marks = int(input(f"Enter Total Marks Acquired for {course_name}: "))
        else:
            midSem_Marks = int(input(f"Enter Your Mid Sem Marks for {course_name}: "))
            internal_Marks = int(input(f"Enter Your Internal Marks for {course_name}: "))
            endSem_Marks = int(input(f"Enter Your End Sem Marks for {course_name}: "))
            course_Marks = midSem_Marks + internal_Marks + endSem_Marks
    except ValueError:
        print("Invalid input for marks. Please enter valid numeric values.")
        break

    if course_Marks < 0 or course_Marks > 100:
        print("Invalid Marks. Marks should be between 0 and 100.")
        break

    coursePoint = math.ceil(course_Marks / 10)
    Credits += coursePoint * course_Credits
    totalCredits += course_Credits

if totalCredits > 0:
    GPA = Credits / totalCredits
    print("Your Credits for this Semester is:", GPA)
else:
    print("GPA calculation aborted due to invalid input.")


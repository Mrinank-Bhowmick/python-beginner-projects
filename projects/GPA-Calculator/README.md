# GPA Calculator

A console tool that computes a semester GPA. It asks for the number of courses, each course's credits, and marks (either a total or split into mid-sem, internal and end-sem), then derives grade points and a weighted GPA.

## Example

```text
------------------------------------------
GPA Calculator:
------------------------------------------
Enter Number Of Courses: 2
Enter 1 to individually enter Mid Sem, Internals & End Sem Marks
Else Enter 0 to enter Total Marks: 0
Enter Course Name: Mathematics
Enter Total Credits Of Mathematics: 4
Enter Total Marks Acquired for Mathematics: 82

Enter Course Name: Physics
Enter Total Credits Of Physics: 3
Enter Total Marks Acquired for Physics: 74

Your Credits for this Semester is: 8.857142857142858
```

## How to run on localhost

```
python GPA-Calculator.py
```

## Dependencies

Standard library only (`math`).

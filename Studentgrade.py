marks = float(input("Enter the student's marks (0–100): "))
if marks >= 90:
    grade = 'A'
elif marks >= 75:
    grade = 'B'
elif marks >= 60:
    grade = 'C'
elif marks >= 50:
    grade = 'D'
else:
    grade = 'Fail'


print(f"The student's grade is: {grade}")
#8. Write a program to find the student with the highest marks from a dictionary.
student_marks = {
    "jhons": 45,
    "abhiram":75,
    "ram":80,
    "ravi":95
}
highest_student = ""
highest_marks = 0

for name,marks in student_marks.items():
    if marks > highest_marks:
        highest_marks = marks
        highest_student = name
print(highest_student)
print(highest_marks)
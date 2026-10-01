import numpy as np
import pandas as pd


student_marks = np.array([78, 85, 92, 68, 90, 74, 88, 96, 81, 70])

print("Student Marks:")
print(student_marks)
print(f"Mean Marks: {np.mean(student_marks):.2f}")
print(f"Median Marks: {np.median(student_marks):.2f}")
print(f"Maximum Marks: {np.max(student_marks):.2f}")
print(f"Minimum Marks: {np.min(student_marks):.2f}")

students = pd.DataFrame({
    'Student ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Student Name': ['Anita', 'Bharat', 'Chetan', 'Divya', 'Esha', 'Farhan', 'Gita', 'Harsh', 'Isha', 'Jatin'],
    'Marks': student_marks
})

print("\nStudents scoring more than 80 marks:")
print(students[students['Marks'] > 80])

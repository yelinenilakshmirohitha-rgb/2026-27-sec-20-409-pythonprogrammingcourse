students = [
    {"name": "Rahul", "marks": 85},
    {"name": "Anjali", "marks": 92},
    {"name": "Amit", "marks": 78}
]

ascending = sorted(students, key=lambda student: student["marks"])
descending = sorted(students, key=lambda student: student["marks"], reverse=True)

print("Ascending order:")
for student in ascending:
    print(student)

print("\nDescending order:")
for student in descending:
    print(student)
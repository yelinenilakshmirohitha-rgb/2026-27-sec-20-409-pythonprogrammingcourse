students = {
    1: {"name": "Rahul", "marks": 85},
    2: {"name": "Anjali", "marks": 92},
    3: {"name": "Amit", "marks": 78}
}

for roll_no, details in students.items():
    print("Name:", details["name"])
    print("Marks:", details["marks"])
    print()

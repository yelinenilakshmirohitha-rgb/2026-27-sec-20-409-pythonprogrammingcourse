student = {
    "name": "Rahul",
    "age": 18,
    "course": "Python"
}

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

print("Name:", student.get("name"))

student.update({"age": 19, "city": "Delhi"})
print("After update:", student)

student.pop("course")
print("After pop:", student)

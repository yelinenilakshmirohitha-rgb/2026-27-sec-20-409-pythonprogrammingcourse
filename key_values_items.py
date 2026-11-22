marks = {
    "English": 85,
    "Maths": 92,
    "Science": 88
}

print("Keys:")
for subject in marks.keys():
    print(subject)

print("\nValues:")
for score in marks.values():
    print(score)

print("\nItems:")
for subject, score in marks.items():
    print(subject, ":", score)
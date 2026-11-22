def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_details(Name="Krishna", Maths=90, Science=85, English=80)
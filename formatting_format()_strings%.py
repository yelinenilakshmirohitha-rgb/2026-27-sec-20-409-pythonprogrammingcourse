name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

# Using format()
print("Using format():")
print("My name is {}, age is {} and marks are {}".format(name, age, marks))

# Using f-string
print("\nUsing f-string:")
print(f"My name is {name}, age is {age} and marks are {marks}")

# Using % operator
print("\nUsing % operator:")
print("My name is %s, age is %d and marks are %.2f" % (name, age, marks))
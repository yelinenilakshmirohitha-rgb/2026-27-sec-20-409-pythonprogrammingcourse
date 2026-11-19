number = int(input("Enter a number: "))

original = number
temp = abs(number)
reversed_number = 0

while temp > 0:
    digit = temp % 10
    reversed_number = reversed_number * 10 + digit
    temp //= 10

if abs(original) == reversed_number:
    print("Palindrome")
else:
    print("Not a palindrome")

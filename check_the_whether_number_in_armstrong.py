# Check whether a 3-digit number is an Armstrong number

n = int(input("Enter a 3-digit number: "))

temp = n
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + (digit * digit * digit)
    temp = temp // 10

if sum == n:
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")
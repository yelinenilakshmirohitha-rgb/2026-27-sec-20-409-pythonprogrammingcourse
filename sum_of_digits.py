n=int(input("Enter a Number:"))

digit_sum=0
while number>0:
    last_digit=number%10
    digit_sum=digit_sum+last_digit
    number=number//10
print(f"sum of digits of {original_num} is {digit_sum}")
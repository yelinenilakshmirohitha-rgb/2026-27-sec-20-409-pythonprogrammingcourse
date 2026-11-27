try:
    a = int(input('Enter a number: '))
    b = int(input('Enter another number: '))
    result = a / b
except ZeroDivisionError:
    print('Error: Cannot divide by zero!')
except ValueError:
    print('Error: Please enter valid numbers!')
else:
    print('Result:', result)
finally:
    print('Program executed successfully!')
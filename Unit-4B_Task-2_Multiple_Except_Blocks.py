try:
    numbers = [10, 20, 30]
    index = int(input('Enter index: '))
    divisor = int(input('Enter divisor: '))
    result = numbers[index] / divisor
    print('Result:', result)
except IndexError:
    print('Error: Index out of range!')
except ZeroDivisionError:
    print('Error: Cannot divide by zero!')
except ValueError:
    print('Error: Please enter valid numbers!')
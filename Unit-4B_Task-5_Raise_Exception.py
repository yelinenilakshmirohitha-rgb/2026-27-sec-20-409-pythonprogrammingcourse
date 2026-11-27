def check_age(age):
    if age < 18:
        raise ValueError('Age must be 18 or above!')
    return 'Access granted!'

try:
    age = int(input('Enter your age: '))
    print(check_age(age))
except ValueError as e:
    print('Error:', e)
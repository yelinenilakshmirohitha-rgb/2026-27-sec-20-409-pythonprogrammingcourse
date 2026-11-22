from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map()
square = list(map(lambda x: x*x, numbers))
print("Squares:", square)

# filter()
even = list(filter(lambda x: x%2 == 0, numbers))
print("Even numbers:", even)

# reduce()
total = reduce(lambda x, y: x+y, numbers)
print("Sum:", total)

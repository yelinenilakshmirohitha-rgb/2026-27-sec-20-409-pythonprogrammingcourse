def add(*args):
    total = 0
    for i in args:
        total = total + i
    return total

print("Sum =", add(10, 20))
print("Sum =", add(10, 20, 30))
print("Sum =", add(5, 10, 15, 20))

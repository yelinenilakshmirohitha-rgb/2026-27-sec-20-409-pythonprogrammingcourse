def rectangle(l, b):
    area = l * b
    perimeter = 2 * (l + b)
    return area, perimeter

l = int(input("Enter length: "))
b = int(input("Enter breadth: "))

a, p = rectangle(l, b)

print("Area =", a)
print("Perimeter =", p)
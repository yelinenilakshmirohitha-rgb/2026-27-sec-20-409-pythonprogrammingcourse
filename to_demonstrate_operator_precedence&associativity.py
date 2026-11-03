# Operator Precedence and Associativity

a = int(input("Enter a Number:"))
b = int(input("Enter a Number:"))
c = a + b * 2
d = (a + b) * 2
e = a - b
print("Precedence:", c)
print("Using Parentheses:", d)
print("Associativity:", e)
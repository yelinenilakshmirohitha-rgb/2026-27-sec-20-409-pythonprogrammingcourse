x=int(input("Enter first Number"))
y=int(input("Enter second Number"))
z=int(input("enter third number"))
if x <= y:
    if x <=z:
        smallest=x
    else:
        smallest=z
else:
    if y<=z: 
        smallest=y
    else:
        smallest=z

print(f"smallest number among{x},{y},{z} is {smallest}")                      
n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    x = int(input())
    if x not in lst:
        lst.append(x)

print("List after removing duplicates:", lst)
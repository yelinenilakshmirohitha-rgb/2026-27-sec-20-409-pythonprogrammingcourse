rows = int(input("Enter number of rows: "))
symbol = input("Enter a symbol: ")

for i in range(1, rows + 1):
    for j in range(i):
        print(symbol, end=" ")
    print()
income = float(input("enter monthly income:"))
food = float(input("enter a food expenses: "))
rent = float(input("enter a travel expenses:"))
other = float(input("enter a other expenses:"))
total_expenses = food + rent + other
expenses  =income - total_expenses
print(total_expenses)
           
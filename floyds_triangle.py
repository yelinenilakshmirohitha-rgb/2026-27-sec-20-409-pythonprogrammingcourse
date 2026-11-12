rows=int (input("Enter number of rows:"))
number=1
for row_loop_var in range(1,rows+1):
    for col_loop_var in range(1,row_loop_var+1):
        print(number,end=" ")
        number=number+1
    print()
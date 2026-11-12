rows=int(input("Enter Number of rows:"))
for row_loop_var in range(1,rows+1):
    for col_loop_var_spaces in range(1,rows-row_loop_var+1):
        print(" ",end=" ")
    for col_loop_var_star in range(1,2*row_loop_var):
        print("*",end=" ")
    print() 
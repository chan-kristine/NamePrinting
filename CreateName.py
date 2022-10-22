

str1 = "TINTIN"
print_T = [[" " for i in range(7)] for j in range(7)]
print_I = [[" " for i in range(7)] for j in range(7)]
print_N = [[" " for i in range(7)] for j in range(7)]

#   CODE FOR T
for row in range(7):
    for col in range(7):
        if row==0 or col==3:
            print_T[row][col]= "*"
           

            
for i in range(7):
    print(end="  ")
    for j in range(7):
        print(print_T[i][j], end=" ")
    print(end="  ")      
    print()
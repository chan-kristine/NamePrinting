# assignment 1 
# Reference in Printing Character  - https://www.youtube.com/watch?v=DOXQn_1aBrY
# Reference in Appplying Color - https://www.youtube.com/watch?v=u51Zjlnui4Y


str1 = "TINTIN"
print_T = [[" " for i in range(7)] for j in range(7)]
print_I = [[" " for i in range(7)] for j in range(7)]
print_N = [[" " for i in range(7)] for j in range(7)]

#   CODE FOR T
for row in range(7):
    for col in range(7):
        if row==0 or col==3:
            print_T[row][col]= "\033[34m*\033[01m"

# CODE FOR I
for row in range(7):
    for col in range(7):
        if row==0 or col==3 or row==6:
            print_I[row][col]= "\033[34m*\033[01m"

# CODE FOR N
for row in range(7):
    for col in range(7):
        if ((col==0 or col==6) or row==col):
            print_N[row][col]= "\033[34m*\033[01m"
            
#   CODE FOR T
for row in range(7):
    for col in range(7):
        if row==0 or col==3:
            print_T[row][col]= "\033[34m*\033[01m"

# CODE FOR I
for row in range(7):
    for col in range(7):
        if row==0 or col==3 or row==6:
            print_I[row][col]= "\033[34m*\033[01m"

# CODE FOR N
for row in range(7):
    for col in range(7):
        if ((col==0 or col==6) or row==col):
            print_N[row][col]= "\033[34m*\033[01m"
            
for i in range(7):
    print(end="  ")
    for j in range(7):
        print(print_T[i][j], end=" ")
    print(end="  ")
    for j in range(7):
        print(print_I[i][j], end=" ")
    print(end="  ")
    for j in range(7):
        print(print_N[i][j], end=" ")
    print(end=" ")
    for j in range(7):
        print(print_T[i][j], end=" ")
    print(end="  ")
    for j in range(7):
        print(print_I[i][j], end=" ")
    print(end="  ")
    for j in range(7):
        print(print_N[i][j], end=" ")
    print(end=" ")
    print()
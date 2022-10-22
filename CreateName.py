# assignment 1 
# Reference in Printing Character  - https://www.youtube.com/watch?v=DOXQn_1aBrY
# Reference in Appplying Color - https://www.youtube.com/watch?v=u51Zjlnui4Y


str1 = "TINTIN"
print_T = [[" " for i in range(13)] for j in range(13)]
print_I = [[" " for i in range(13)] for j in range(13)]
print_N = [[" " for i in range(13)] for j in range(13)]

#   CODE FOR T
for row in range(13):
    for col in range(13):
        if row==0 or col==6:
            print_T[row][col]= "\033[34m*\033[01m"

# CODE FOR I
for row in range(13):
    for col in range(13):
        if row==0 or col==6 or row==12:
            print_I[row][col]= "\033[34m*\033[01m"

# CODE FOR N
for row in range(13):
    for col in range(13):
        if ((col==0 or col==12) or row==col):
            print_N[row][col]= "\033[34m*\033[01m"
            
#   CODE FOR T
for row in range(13):
    for col in range(13):
        if row==0 or col==6:
            print_T[row][col]= "\033[34m*\033[01m"

# CODE FOR I
for row in range(13):
    for col in range(13):
        if row==0 or col==6 or row==12:
            print_I[row][col]= "\033[34m*\033[01m"

# CODE FOR N
for row in range(13):
    for col in range(13):
        if ((col==0 or col==12) or row==col):
            print_N[row][col]= "\033[34m*\033[01m"
            
for i in range(13):
    print(end="  ")
    for j in range(13):
        print(print_T[i][j], end=" ")
    print(end="  ")
    for j in range(13):
        print(print_I[i][j], end=" ")
    print(end="  ")
    for j in range(13):
        print(print_N[i][j], end=" ")
    print(end=" ")
    for j in range(13):
        print(print_T[i][j], end=" ")
    print(end="  ")
    for j in range(13):
        print(print_I[i][j], end=" ")
    print(end="  ")
    for j in range(13):
        print(print_N[i][j], end=" ")
    print(end=" ")
    print()
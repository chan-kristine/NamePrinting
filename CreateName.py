# assignment 1 
# Reference  - https://www.youtube.com/watch?v=DOXQn_1aBrY

str1 = "TINTIN"
print_T = [[" " for i in range(7)] for j in range(7)]
print_I = [[" " for i in range(7)] for j in range(7)]
print_N = [[" " for i in range(7)] for j in range(7)]

#   CODE FOR T
for row in range(7):
    for col in range(7):
        if row==0 or col==3:
            print_T[row][col]= "*"

# CODE FOR I
for row in range(7):
    for col in range(7):
        if row==0 or col==3 or row==6:
            print_I[row][col]= "*"

# CODE FOR N
for row in range(7):
    for col in range(7):
        if ((col==0 or col==6) or row==col):
            print_N[row][col]= "*"
            
#   CODE FOR T
for row in range(7):
    for col in range(7):
        if row==0 or col==3:
            print_T[row][col]= "*"

# CODE FOR I
for row in range(7):
    for col in range(7):
        if row==0 or col==3 or row==6:
            print_I[row][col]= "*"

# CODE FOR N
for row in range(7):
    for col in range(7):
        if ((col==0 or col==6) or row==col):
            print_N[row][col]= "*"
            
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
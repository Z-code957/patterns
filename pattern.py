"""print("creating half pyramid pattern")
n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()"""
n = int(input("Enter the number of rows: "))
number = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(number,end=" ")
        number = number+1
    print()
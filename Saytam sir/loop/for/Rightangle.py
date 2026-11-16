for i in range(1,6):
    for j in range(0,i):
        print("*",end=" ")
    print()
    

n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    print("* " * i)

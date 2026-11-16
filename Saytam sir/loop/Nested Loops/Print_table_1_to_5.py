
s = int(input("Enter the table range start "))
n = int(input("Enter the table range end "))

for i in range(s,n+1):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")
    print("-----------------------")  
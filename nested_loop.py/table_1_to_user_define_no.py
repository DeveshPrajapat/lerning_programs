first = int(input("Enter the first table number "))
second = int(input("Enter the Second table number "))

for i in range(first, second+1):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")
    print("==================================")
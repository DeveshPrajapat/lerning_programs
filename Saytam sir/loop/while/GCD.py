n1 = int(input("Enter the Number 1 "))
n2 = int(input("Enter the Number 2 "))


while n2!=0:
    n1,n2, = n2,n1%n2

print(f"GCD of the two Numbers is : {n1}")
    
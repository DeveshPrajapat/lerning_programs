n1 = int(input("enter first number "))
n2 = int(input("enter second number "))
print("Chosse from below options")
print("1 for Addition")
print("2 for Subration")
print("3 for multiplication")
print("4 for division")
ch = int(input("enter choices number "))
print("----------------------------------")

match ch:
    case 1:
        print(f"addtion {n1+n2}")
    case 2:
       print(f"sub {n1-n2}")
    case 3:
        print(f"multi {n1*n2}")
    case 4:
        print(f"div {n1/n2}")
    case _:
        print("default value")
st = input("Enter the String ")

upper = 0
lower = 0

for char in st:
    if char.isupper():
        upper = 1
    elif char.islower():
        lower = 1

if upper and lower:
    print("Yes")
else:
    print("No")
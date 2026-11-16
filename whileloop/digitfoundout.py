num = int(input("Enter any number "))
c = 0
while num > 0:
    num = num//10
    c+=1
print(f"Number of digit is {c}")

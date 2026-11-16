num = int(input("Enter any number "))
sum = 0
while num != 0:
    r = num%10
    sum=sum*10+r
    num = num//10
print(f"Number of digit is {sum}")

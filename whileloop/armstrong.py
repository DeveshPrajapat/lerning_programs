num = int(input("Enter any number "))
c = 0
g = num
sum = 0
o = num
while num > 0:
    num = num//10
    c+=1
while g !=0:
    r = g%10
    sum = r**c+sum
    g = g//10  

if o == sum:
    print(f"{sum} is Armstrong Number ")
else:
    print(f"{o} Number is not Armstrong ")
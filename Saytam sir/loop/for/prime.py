n = int(input("Enter the Number "))
c = True
if n <=1:
    c = False
else:
    for i in range(2,n):
        if n%i == 0:
            c = False
            break
if c:
    print("Number is Prime ",n)
else:
    print("Number is not Prime",n)

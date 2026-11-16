a = int(input("Enter the First Term "))
r = int(input("Enter the Common Ratio "))
n = int(input("Enter the Term Number "))

i = 1
an = a

while i <= n :
    print(an,end=" ")
    an = an*r
    i+=1
   
    

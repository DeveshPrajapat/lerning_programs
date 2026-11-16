num = int(input("Enter any number "))
c=0
n = num
for i in range(1,num+1):
    if num%i==0:
        r = num//i
        print(f" {n} Factors {r}")
        c+=1
        
print(f"Max factor of number {c}")
n = 123
r = 0
while n > 0:
    q = n%10
    r = q+r*10 
    n = n//10
print(r)
    
    
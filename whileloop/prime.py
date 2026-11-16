# Adnan logic
'''num = int(input("Enter any number "))
c = 0

for i in range(2,num+1):
    if num % i  == 0:
        c+=1

if c == 1 :
    print("Prime") 
    
else:
    print("NOt Prime")
        '''
        
# Coaching logic

num = int(input("Enter any number "))
flag = False

for i in range(2,num):
    if num % i  == 0:
        flag = True
        break
      

if flag :
    print("Not Prime") 
    
else:
    print("Prime")
    

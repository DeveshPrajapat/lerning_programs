# li = [1,2,33,54,87.99,12,54,3,4,5,6]

# for i in li:
#     if i % 2 == 0:
#         print(f"{i} Even")
#     else:
#         print(f"{i} odd")



li = [11,12,33,14,15,76,47,98,39]

num = int(input("Enter target number "))
c = 0

# My logic

for i in li:
    if num == i :
        c+=1
        break
    
if c == 1:
    print(f"{num} is found")
else:
    print(f"{num} is found")

# Sir logic

# if num in li :
#     print(f"{num} is in the list ")
    
# else:
#     print(f"{num} is not in the list ")
   
    
        

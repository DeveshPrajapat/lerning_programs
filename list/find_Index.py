li = [123,42,43,54,75,86,67,80,97]

num = int(input("Enter target number "))
c = 0

# My logic

for i in range(len(li)):
    if li[i] == num :
        c+=1
        break
    
if c == 1:
    print(f"{num} is found and index is {i}")
else:
    print(f"{num} is not found ")
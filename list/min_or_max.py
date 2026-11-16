# li = [111,2,3,4,89,5,6,7,8,9]
# mi = li[0]
# mx = li[0]

# for i in range(1,len(li)):
#     if li[i] < mi:
#         mi = li[i]
#     if li[i] > mx :
#         mx = li[i]
        
# print(f"the minimum number in list is : {mi}")
# print(f"the maximum number in list is : {mx}")


#! Second Minimum and second Maximum 

newli = [12,2,34,55,5,67,23,1,456,55555]
min = newli[0]
max = newli[0]

for i in range(1,len(newli)):
    if newli[i] < min :
        min = newli[i]
    if newli[i] > max :
        max = newli[i]

secmin = max
secmax = newli[0]

for i in range(1,len(newli)):
    if newli[i] < secmin :
        secmin = newli[i]
    if newli[i] > secmax :
        secmax = newli[i]
        
print(f"Minimum number of list is {min}")
print(f"Second Minimum number of list is {secmin}")
print("==================================")
print(f"Maximum number of list is {max}")
print(f"Second Maximum number of list is {secmax}")
















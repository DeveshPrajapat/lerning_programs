li = ["Hello","Morning","Boy","Singapore","School"]
mi = li[0]
mx = li[0]

for i in range(len(li)):
     if li[i] < mi:
        mi = li[i]
     if li[i] > mx :
        mx = li[i] 
        
print(f"the minimum number in list is : {mi}")
print(f"the maximum number in list is : {mx}")
        
        
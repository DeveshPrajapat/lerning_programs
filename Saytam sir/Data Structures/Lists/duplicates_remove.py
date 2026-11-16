li = [1,2,3,4,5,1,6,7,8,9,11,2,4,8]

new_li = []

for i in li:
    if i not in new_li:
        new_li.append(i)
      
print(new_li)
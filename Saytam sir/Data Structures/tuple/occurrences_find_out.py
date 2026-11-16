tup = (10, 20, 30, 40) 
element = 50
found = False
for i in range(len(tup)):
    if tup[i]== element:
        found = True
        break
    
if not found:
    print("Element not found ")
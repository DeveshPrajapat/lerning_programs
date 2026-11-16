# Make a tuple and take inpyt from user if the number exists in the tuple remove it if not append it
# tup = (1,2,4,6,7,9)
# num = int(input("Enter any Number "))
# temp = list(tup)
# if num in tup:
    
#     temp.remove(num)
#     tup = tuple(temp)
#     print(f"Remove exists number {tup}")
# else:
    
#     temp.append(num)
#     tup = tuple(temp)
#     print(f"Append number {tup}")
    
#! WAP to get the 4th element from the last element of a tuple

# tup_4th = (11,12,1314,23,234,45,56,667,89,100)
# print(tup_4th[-4])

#? WAP Program to replace the last value of tuple in a list 

li = [(10,20,30),(40,50,60),(70,80,90)]
# My logic
# new = []
# for i in li:
#     temp = list(i)
#     temp[2] = 100
#     li = tuple(temp)
#     print(li)

# ! Sir Logic
print([t[:-1]+(100,) for t in li])# for t in li -> Means we are accessing the tuples inside of list one at a time  [:-1] + (100,) Means stroe the value of 0th and 1st index that are by concatinate the last index with 100  
    
   
    
    
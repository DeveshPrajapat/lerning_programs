#  Count Strings with Same Start and End

# li = ["abc","xyz","aba","1221"]
# c=0
# for i in li:
#     if len(i)>1 and i[0] == i[-1]:
#         print(i)
#         c+=1
# print(c)

# ! Remove Duplicates from List

# li = [10,20,30,40,50,20,60,30,90]
# newi = []

# for i in li:
#     if i not in newi:
#         newi.append(i)
# print(newi)

#? Multiply items in list

# muli = [3,5,2,9,4]
# multiple_list = 1
# for i in muli:
#     multiple_list *= i
# print(f"Multiple of list element = {multiple_list}")

# TODO :- Check common Member between Two lists 

# li1 = [1,2,3,4,5,6,7,8]
# li2 = [6,7,8,9,10,11,12,14]
# li3 = []

# for i in li1:
#     for j in li2:
#         if i == j:
#             li3.append(i)
# print(li3)

#?  
# li = [3,6,9,6,7,1,2,8,8,3,8,45,6,3,2,1]
# li1 = [li[0]]
# for i in li[1:]:
#     if i > li1[-1]:
#         li1.append(i) 
    
# print(li1)

# ! List se sirf even numbers uthao, order same rakho

# li = [5,2,7,8,3,10,4]

# for i in li:
#     if i%2 != 0:
#         li.remove(i)

# print(li)

# TODO List se strictly increasing sequence banao

# li = [1,3,2,4,3,5]
# li1 = [li[0]]
# for i in li[1:]:
#     if i > li1[-1]:
#         li1.append(i)
# print(li1)

 #? List ke numbers ko continuous number bana do

# li = [1,20,3,4]

# for i in li:
#     print(i,end="")


#! list se duplicate hata ke order same rakho

# li = [1,2,1,3,2,4]
# du_li = []
# for i in li :
#     if i not in du_li:
#         du_li.append(i)

# print(du_li)

# TODO List se non-decreasing subsequence banao (>= allowed)

# li = [3,3,2,4,4,1,5]
# newli = [li[0]]

# for i in li[1:] :
#     if i >= newli[-1]:
#         newli.append(i)
# print(newli)

#? List me se sirf digits (0–9) uthao, baaki ignore karo
# li = [12,3,45,6,7,9,89,2]
# newli = []
# for i in li :
#     if 0 < i <= 9 :
#         newli.append(i)
# print(newli)

#! List se aisi subsequence banao jisme har next number previous ka multiple ho

# li = [2, 4, 3, 6, 12, 5, 10]

# newli = [li[0]]

# for i in li[1:] :
#     if i % newli[-1] == 0:
#         newli.append(i)

# print(newli)

#? # List se aisi subsequence banao jahan har next number previous se kam ho (strictly decreasing) 

li = [9, 7, 8, 5, 6, 3, 4, 2]

newli = [li[0]]

for i in li[1:]:
    if i < newli[-1]:
        newli.append(i)
print(newli) 

#TODO List se longest increasing subsequence nikaalo

li = [10, 9, 2, 5, 3, 7, 101, 18]

newli = [li[0]]

for i in li :
    for j in li[1:]:
        if j < i:
            j , li[i] = j , li[i]

print(li)
            

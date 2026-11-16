# Wirte a code to sort a list without using sort function

# my bybble sort 

# li = [12,4,16,8,19,14,4,3,1,5,7]
# tem =0

# for i in range(0,len(li)):
#     for j in range(0,len(li)):
#         if li[i] < li[j]:
#             tem = li[i]
#             li[i] = li[j]
#             li[j] = tem
# print(li)

# Sir bubble sort 

# li = [12,4,16,8,19,14,4,3,1,5,7] 
# print("Orignal\n",li)
# for i in range(len(li)-1):
#     for j in range (len(li)-i-1):
#         if li[j] > li[j+1]:
#             li[j],li[j+1] = li[j+1],li[j]
# print(li)


# ! Write a code to check if all the numbers in the list is prime or not 

li = [2,3,4,5,7]
flag = False
for i in range(len(li)):
    for j in range(2,i):
        if li[i]%j == 0:
            flag = True
            break
    break
    
if flag:
    print(flag)
else:
    print(flag)


    


# * Wirte a code to remove all the duplicate elements of list 

# li = [34, 67, 8, 3, 8, 3, 56, 879, 3, 123, 8]

# newli = []

# for i in li:
#     if i not in newli:
#         newli.append(i)
# print(f"Remove all duplicate {newli}")

# # ? Write a code to merge two lists

# li = [12,4,16,8,19,14,4,3,1,5,7]
# li2 = [1111,2222]

# print(li + li2)

# TODO  Write a code to store all the even and odd numbers of a list into another list

# li = [1,2,3,4,5,6,7,8,9]
# even_li = []
# odd_li = []

# for i in li:
#     if i%2 == 0:
#         even_li.append(i)
#     else:
#         odd_li.append(i)
# print("List of Even Numbers")
# print(even_li)
# print("=======================")
# print("List of Odd Numbers")
# print(odd_li)






# ! Write a code to take input of a number and check if it has repeating digits

# li = [0,0,0,0,0,0,0,0,0,0]
# num = int(input("enter any number "))
# rem = 0

# while num > 0:
#     rem = num%10
#     if li[rem] == 1:
#         break
#     li[rem] = 1
#     num = num // 10
    
# if num > 0:
#     print(f"{rem} Yes")
# else:
#     print(f"No")


 

























# TODO MCQs 

# ?1. What will be the output of the following code?
# x = 5
# y = 10
# x, y = y, x + y
# print(x, y)

# # A. 10 15

# # What is the output of this code?
# def func(a, L=[]):
#     L.append(a)
#     return L

# print(func(1))
# print(func(2))
# print(func(3))

# # B. [1],[1,2],[1,2,3]

# # What is the output of this code?
# a = [1, 2, 3]
# b = a
# a.append(4)
# print(b)

# # B.[1,2,3,4]

# # What is the type of the result of:
# type(5 / 2)

# B. float
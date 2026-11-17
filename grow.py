# num = int(input("Enter the number "))
# a = 0 
# b = 1 
# if num == 1 :
#     print(0)
# else:
#     for i in range(num+1):
#         print(a)
#         c = a+b
#         a = b
#         b = c 
        
        
# TODO second high. number 

# a = [45,4,56,86,65,78,264,60,200,264.5,25,265,24]

# b = a[0]

# for i in a :
#     if b < i:
#         b = i
 
# print("largest ",b)
# se = b

# for i in a:
#     if se > i:
#         se = i
# print("small   ",se)

# for i in a:
#     if se < i and b > i:
#         se = i
# print("Second Largest ",se)

# ? Reverse string without using function

# l = [80, 70, 60, 50, 40, 30, 20, 10]
# le = len(l)
# la = []

# for i in range(le-1,-1,-1):
#     la.append(l[i])

# print(la)

    
 # ! Count Even and Odd Numbers 
 
# a = [12, 45, 67, 80, 22, 31, 44, 55, 90, 11]

# even = []
# odd = []
# even_count = 0
# odd_count = 0

# for i in a:

#     if i%2 == 0:
#         even.append(i)
#         even_count+=1
#     else:
#         odd.append(i)  
#         odd_count+=1
        
# print(f'Even count {even_count} even Number {even}')
# print(f'odd count {odd_count} odd Number {odd}')


# ! Find Duplicate Numbers

# a = [10, 20, 30, 20, 40, 50, 10, 60, 30, 70]
# a_count = 0
# l = []
# la = []
# for i in a:
#     if i not in l:
#         l.append(i)  
#     elif i not in la:
#         la.append(i)
#         a_count +=1 
        
# print(la)
# print(a_count)

# TODO Find Frequency of Each Element


# a = [10, 20, 10, 30, 20, 10, 40, 30, 20]
# freq = {}
# for i in a :
#     if i in freq :
#         freq[i] +=1
#     else:
#         freq[i] = 1

# print(freq)


# # ? Find First Non-Repeating Element


# a = [10, 20, 30, 10, 20, 40, 50, 30]

# freq = {}
# la = []
# for i in a:
#     if i in freq :
#         freq[i] +=1
#     else:
#         freq[i] = 1 
        
# for i in freq:
#     if freq[i] == 1:
#         la.append(i)
        
# print(la[0])
# print(la)

#! Topic: Two Sum Problem

# a = [2, 7, 11, 15, 3, 6]
# target = 9
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]+a[j] == target:
#             print(f'{a[i]} + {a[j]} = {target },index {i},{j}')
        
# TODO Move Zeros to end
# a = [0, 1, 0, 3, 12, 0, 5, 8]
# li = []
# la = []
# for i in a:
#     if i  == 0:
#         la.append(i)
#     else:
#         li.append(i)
# print(li + la)


# ? Find Missing Number

a = [1, 2, 3, 5, 6, 7, 8, 9, 10]
for i in range(1,11):
    if i not in a:
        print("Missing number : ", i)
        break
        
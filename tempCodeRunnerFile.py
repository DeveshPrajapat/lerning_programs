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
# Largest numbers 

# li = [20,40,50,49,60,22]
# l = li[0]
# for i in li:
#     if i > l:
#         l = i
# print(l)

# Frequency of each element
# li = [1,2,3,4,5,6,6,3,1]
# l = []
# for i in li :
#     c = li.count(i)
#     l.append(c)

# print(l)

# li = [1,2,3,4,5,6,6,3,1]

# s = list(set(li))
# print(s)

# li = [1,2,3,4,5,6,66,3,1]
# lar = li[0]

# for i in li:
#     if lar < i:
#         lar = i
# se_lar = li[0]
# for i in li:
#     if lar > i:
#         se_lar = i

# print(se_lar)

# st = "11211"
# og = st
# p = st[::-1]
# if og == p:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
        

# arr1 = [1, 2, 4, 5, 7] 
# arr2 = [5, 6, 3, 4, 8] 
# x = 9

# for i in arr1:
#     for j in arr2:
#         if i+j == x:
#             print(i,j)

# dic1 = {"A":1,"B":2,"C":3}
# dic2 = {"D":4,"E":5,"F":6}

# print(dic1 | dic2)

from collections import defaultdict

w = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagrams = defaultdict(list)

for word in w:
    key = ''.join(sorted(word))
    anagrams[key].append(word)

print(list(anagrams.values()))
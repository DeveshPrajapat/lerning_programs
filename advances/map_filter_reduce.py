from functools import reduce
# def sqr(x):
#     return x * x

# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_li = []

# for i in li:
#     new_li.append(sqr(i))
    
# print(new_li)

# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_li = list(map(lambda x: x * x, li))
# print(new_li)

# def even(x):
#     if x % 2 == 0:
#         return x

# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_li = []

# for i in li:
#     new_li.append(even(i))
    
# print(new_li)

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_li = list(filter(lambda x: x % 2 == 0, li))
print(new_li)
# 2 4 6 8 10
value = reduce(lambda x, y: x + y, new_li)
print(value)
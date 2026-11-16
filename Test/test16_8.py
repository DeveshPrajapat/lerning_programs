# 1. Given a nested list [[1,2,3],[4,5,6],[7,8,9]], flatten it into [1,2,3,4,5,6,7,8,9].

# li = [[1,2,3],[4,5,6],[7,8,9]]
# print(li[0]+li[1]+li[2])

#! 2. Write a program to find the index of the maximum element in a tuple.
 
# tup = (1,2,3,45,67,9,56,23,55,99)
# max = tup[0]
# for i in range(len(tup)):
#     if tup[i]> max:
#         max = tup[i]
#         new = i
# print(f"Maximum index {new}")
    

#? 3. Write a program that accepts a number n and prints a list of all its divisors

# li = [2,3,4,5,6,7,8,99,200,1,34,80]
# newli = []
# num = int(input("Enter a number "))

# for i in li:
#     if num % i == 0:
#         newli.append(i)
        
# print(newli)

#TODO 4. Write a function that accepts a tuple of numbers and returns a new tuple with only even numbers.

tup = (1,2,3,4,5,6,7,8,9,12,14,35)
li = list(tup)
newli = []

for i in li:
    if i%2 == 0:
        newli.append(i)

tup = tuple(newli)
        
print(tup)

# ! 5. Given a tuple (10,20,30,40), swap first and last elements → (40,20,30,10).

tup = (10,20,30,40)
# l = len(tup)
# f=tup[0]

swap= (tup[-1],) + tup[1:-1]+(tup[0],)

print(swap) 







       
        





# Write a program to merge two dictionaries. If a key exists in both, add rhir values.
# dict1 = {"a":10,"b":20,"c":30}
# dict2 = {"d":5,"c":15,"e":23}

# dict1.update(dict2)
# print(dict1)

# Check Key Existence in Dictionary.Write a Python script to check whether a given key already exists in a dictionary.


# dic =  {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# key = int(input("Enter any key here in number form :-"))

# def is_key_present(key):
#     if key in dic:
#         print("Key is present in Dictionary ")
#     else:
#         print("Key is not present in dictionary ")
# is_key_present(key)

# ! Iterate Over Dictionary Using For Loops

# dic =  {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# for key , value in dic.items():
#     print(f"key is {key} and value is {value}")


# ?Merge Two Python Dictionaries

# d1 = {'a':100,'b':200}
# d2 = {'c':300,'d':400}
# d3 = {}

# for i,j in d1.items():
#     d3[i] = j  
# for k,l in d2.items():
#     d3[k] = l

# print(f"Add two Dictionary in {d3}")

#  Merge Two dictionary if same key is present so, add there value in single vale d1 = {'a':100,'b':200,'c':50},d2 = {'c':300,'d':400} result is 


d1 = {'a':100,'b':200,'c':50}
d2 = {'c':300,'d':400}
d3 = {}

for i,j in d1.items():
    
    for k,l in d2.items():
       if i == k:
           j = j+l
    d3[i] = j
    d3[k] = l
           
print(f"Merge two dictionary and Value too {d3}")
    
# TODO Sum All Items in a Dictionary
# d = {'a':100,'b':200,'c':50}

# def sum(d):
#     sum = 0
#     for i in d.values():
#         sum +=i
    
#     return sum
    


# print(f"Sum of all dictionary {sum(d)}")

# !Multiply All Items in a Dictionary

# d = {'a':100,'b':-54,'c':247}

# def multi(d):
#     multi = 1
#     for i in d.values():
#         multi *=i
    
#     return multi
    


# print(f"Sum of all dictionary {multi(d)}")

#! Get Maximum and Minimum Values of a Dictionary

d = {'a':1,'b':55,'c':3,'d':4}
max = 1

for i in d.values():
    if max<i :
        max = i

print(max)
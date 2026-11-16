# 1.	Write a Python program to count the number of characters (character frequency) in a string. 
# Sample String : google.com' 
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1} 

# str = input("Enter a string ")
# d = {}
 
# for i in str:
#     c = 0
#     for j in str :
#         if i == j:
#             c+=1
#     d[i] = c
# print(d) 
        

#TODO 2.	Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. 
# Sample String : 'restart' 
# Expected Result : 'resta$t' 

# str = input("Enter the string ")
# new_str = str[0]

# for i in range(1,len(str)):
#     if str[0] == str[i]:
#         new_str += "$"
#     else:
#         new_str +=str[i]
    
# print(new_str)


        
#? 3.	Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. 
# ?Sample String : 'abc' 
# ?Expected Result : 'abcing' 
# ?Sample String : 'string' 
# ?Expected Result : 'stringly 

# str = input("Enter a string ")

# if str[-3:] == "ing":
#     print(str+"ly")
# else:
#     print(str+"ing")

        
#! 4.	Write a Python program to change a given string to a newly string where the first and last chars have been exchanged. 

# str = input("Enter a string ")
# s = str[0]
# l = len(str)
# l = str[l-1]
# print(l+str[1:-1]+s)

# ? 5.	Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead. Sample String : 'w3resource' 
# Expected Result : 'w3ce' 
# Sample String : 'w3' 
# Expected Result : 'w3w3' 
# Sample String : ' w' 
# Expected Result : Empty String 

# str = "w3"
# le = len(str)
# if le < 2:
#     print(f"string is empty {str}")
# else:
#     print(str[:2]+str[-2:])

# ! Reverse string save in new string

# str = input("Enter any string ")

# s = str[::-1]

# print(s)

# ? palindrom

# str = input("Enter any string ")
# pali_str = str[::-1]

# flag = False

# for i in range(len(str)):
#     if str[i] != pali_str[i]:
#         flag = True
#         break

# if flag :
#     print("Not Palindrom")
# else:
#     print("Palindrom")


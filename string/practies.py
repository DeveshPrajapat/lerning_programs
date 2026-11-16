# Calculate string length
# def strlen(str):
#     c = 0
#     for i in str:
#         c +=1
#     return c

# str = input("Enter the any string ")

# s = strlen(str)
# print(f"Length of string is {s}")

#! Count character frequency in a string.

# def count_character(str):
#     d = {}
#     for i in str:
#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = 1
#     return d

# print(count_character('google'))

# TODO Get string of first and last 2 chars.

# def first_and_last_char(str):
#     l = len(str)
    
#     if l < 2 :
#         return "Empty string "
#     else:
#         return (str[:2]+str[-2:])
    

# print(first_and_last_char("w3cdlkfjsde"))
# print(first_and_last_char("w3"))
# print(first_and_last_char("w"))
# print(first_and_last_char(""))

#? Replace first char occurrences with $.

# def first_char(str):
#     new_str = str[0]
#     for i in range(1,len(str)):
#         if new_str[0] == str[i] :
#             new_str += "$"
#         else:
#             new_str += str[i]
            
#     return new_str
            
# print(first_char("racecar"))
# print(first_char("evesh"))

#  Remove nth character from a string

# def remove_nth(str,n):
#     before_remove =str[:n] 
#     after_remove = str[n+1:]
#     return before_remove+after_remove

# print(remove_nth("python",2))

#! Capitalize first letter in string 
# str = input("Enter any string ")

# if 'a' <= str[0] <="z":
#     s  = chr(ord(str[0])-32) + str[1:]
#     print(s)

# s = input("Enter any string: ")
# result = ""
# upper_case = True

# for ch in s:
#     if upper_case and 'a' <= ch <= 'z':
#         result += chr(ord(ch)-32)
#         upper_case = False
#     else:
#         result += ch
#         if ch == " ":
#             upper_case = True

# print(result)
    
# ? Add hashes around non-vowels.

# def test(text):
#     return "".join([el, '-' + el + '-'][el not in "AEIOUaeiou"] for el in text)


# text = "Green"
# print("Original string:", text)

# print("Insert Hash elements on both sides of each element, which are not vowels:")
# print(test(text))

# text = "White"

# # Print the original string
# print("\nOriginal string:", text)

# # Print a message indicating the insertion of hash elements
# print("Insert Hash elements on both sides of each element, which are not vowels:")

# # Call the function to modify the string and print the resultaaa
# print(test(text))

# ! Non repeating string charcter example "aabbcdd" , output is "c"

# str = input("Enter any string ")
# s = ""
# for i in range(len(str)):
#     if str[i] not in s:
#         s+=str[i]
        
#     else:
#         s = ""
    
# print(s)


# ? Bubble sort  in string

str = input("Enter any string ")
str = list(str)
for i in range(len(str)-1):
    for j in range(0,len(str)-i-1):
        if str[j] > str[j+1]:
            str[j],str[j+1] = str[j+1],str[j]
print(str)


            
            
    
    


    
            

    

    
# Reverse String 

# str = "Devesh"
# print(str[::-1])


# Count Vowels 

t = input("Enter a string ").lower()
count = 0
for i in t:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" :
        count +=1

print(f"there are so many vowels {count}")
    
# Swap two numbwers without temp 

a = 10
b = 20

a,b = b,a
print(f"a {a} b {b}")
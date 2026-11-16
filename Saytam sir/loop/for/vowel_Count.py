text = input("Enter the string ").lower()

count = 0

for i in text:
    if i in "aeiou":
        count+=1
print(f"Number of Vowel is {count}")
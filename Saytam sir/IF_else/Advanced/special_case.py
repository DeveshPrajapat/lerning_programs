text = input("Enter the number: ")

if text.isalpha():
    print("Alphabet")
elif text.isdigit():
    print("Digit")
else:
    print("Special Character")
 
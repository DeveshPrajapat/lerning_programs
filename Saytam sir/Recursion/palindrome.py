def palin(str):
    """Palindrome check of word"""
    if len(str) <= 1:
        return True
    if str[0] != str[-1]:
        return False
    return  palin(str[1:-1])

str = input("Enter your String ")

if palin(str):
    print("Palindrome")
else:
    print("Not Palindrome")
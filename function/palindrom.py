def palindrom ():
    num = int(input("Enter any number "))
    result = num
    sum = 0
    while num != 0:
        rem = num%10
        sum = sum*10+rem
        num = num//10
    if result == sum:
        print(f"Number is palindrome {result}")
    else :
        print(f"Number is not Palindrome")
        
palindrom()
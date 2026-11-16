num = int(input("Enter any number "))

if num%3 == 0 and num%5 == 0 :
    print("fizz Buzz")
elif num%3 == 0:
    print("fizz")
elif num%5 == 0:
    print("buzz")
else:
    print(f"Not vaild ")
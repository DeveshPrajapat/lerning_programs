year = int(input("Enter your Year "))
 
if year % 100 == 0 :
    if year % 400 == 0 :
        print(f" This is Leep Year {year}")
    else:
        print(f"This is not a leep Year {year}")

else:
    if year % 4 == 0:
        print(f"This is a leep year {year}")
    else:
        print(f"This is not a leep Year {year}")
    
num = int(input("Enter the number: "))

if num <= 1:
    print("Not Prime")
else:
    if num == 2:
        print("Prime")
    else:
        if num % 2 == 0:
            print("Not Prime")
        else:
            if num % 3 == 0 and num != 3:
                print("Not Prime")
            else:
                if num % 5 == 0 and num != 5:
                    print("Not Prime")
                else:
                    print("Prime")

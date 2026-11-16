for num in range (1,501):
    sum = 0
    original = num
    while num != 0:
        r = num%10
        sum=sum*10+r
        num = num//10

    if original == sum:
        print(f"Numberis Palindrome {sum}")

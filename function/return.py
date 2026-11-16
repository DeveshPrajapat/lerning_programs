# return define :- function ki value ko function ke bahar use kar paye

def digit_counter():
    num = int(input("Enter a number "))
    c = 0
    while num != 0:
        num = num // 10
        c+=1
    
    return c

def prime_number (num):
    flag = False
    for i in range(2,num):
        if num%i == 0:
            flag = True
            break
    if flag == True:
        print(f"{num} is Composite")
    else:
        print(f"{num} is a prime ")
    
prime_number(digit_counter())
from random import randint

random_num = randint(1, 1000)
count = 0

while True :
    num = int(input("Guess the  number "))
    if random_num == num:
        count +=1
        print(f"Find out {num} in time {count}")
        break
    elif random_num > num:
        print(f"Number is smaller")
        count +=1
    else:
        print(f"Number is greater")
        count +=1
    
        
    
        
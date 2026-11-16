from random import randint

random_num = randint(1,3)

choices = (input("Your turn \n 1. Rock \n 2. Paper \n 3. Scissor \n"))

if choices == random_num :
    print("Match Draw")
    print(f"Rondom {random_num}")

elif choices == "rock":
    if random_num == "scissor":
        print(f"computer choice {random_num}\nyou choices {choices}")
        print(" u Win ")
        
    else:
         print(f"computer choice {random_num}\nyou choices {choices}")
         print(" lose ")
elif choices == "paper":
    if random_num == "rock":
        print(f"computer choice {random_num}\nyou choices {choices}")
        print(" u Win ")
    else:
         print(f"computer choice {random_num}\nyou choices {choices}")
         print(" lose ")

elif choices == "scissor":
    if random_num == "paper":
        print(f"computer choice {random_num}\n you choices {choices}")
        print(" u Win ")
        
    else:
         print(f"computer choice {random_num}\n you choices {choices}")
         print("lose ")
         

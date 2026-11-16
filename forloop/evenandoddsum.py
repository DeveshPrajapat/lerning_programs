num = int(input("Enter any number "))
sum = 0 
for i in range(1 , num+1):
    if i%2 ==0:
        sum+=i
        print(f"{i} Even number") 
print(f"Sum of Even number is {sum}")
print("-------------------------------------")
add = 0
for i in range(1 , num+1):
    if i%2 !=0:
        add+=i
        print(f"{i} Odd number") 
print(f"Sum of Odd number is {add}")
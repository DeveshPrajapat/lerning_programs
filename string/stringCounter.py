# str = input("Enter your string ")
# low = 0
# upp = 0
# spe = 0
# nu = 0
# for i in str:
#     if 'a' <= i <='z':
#         low +=1
#     elif 'A' <= i <= 'Z':
#         upp +=1
#     elif '0' <= i <='9':
#         nu +=1
#     else:
#         spe+=1

# print(f"Lower case {low}\nUpper case {upp}\nNumbers {nu}\nSpecial Charcters {spe} ")        

# Stirng Counter



str = input("Enter a string ")
c = 0
for i in str:
    c+=1

print(f"Number of string is {c}")

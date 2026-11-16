dic = {"Name":"Devesh","Age":20,"skill":"Django"}

key = input("Enter a key ")
# c = 0
# for i in dic:
#     if i == key:
#         c +=1
#         break
# if c == 1:
#     print("Yes")
# else:
#     print("No")
    
if key in dic:
    print(f"key is in dictionary ")
else:
    print(f"No ")
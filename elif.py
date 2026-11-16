# tem = int(input("Enter Temp. "))

# if tem<0:
#     print("Freezing Weather")
# elif 0<= tem < 10:
#     print("Very Cold Weather")
# elif 10<= tem < 20:
#     print(" Cold Weather")
# elif 20<= tem < 30:
#     print("Normal Weather")
# elif 30<= tem < 40:
#     print("It's Hot") 
# else:
#     print(" It's Very Hot Weather")


t1 = int(input("Enter first angle "))
t2 = int(input("Enter second angle "))
t3 = int(input("Enter thrid angle "))

if t1 == t2 and t2 == t3:
    print(" equilateral")
    
elif t1 == t2 or t2 == t3 or t1 == t3:
    print("Isosceles")

else:
    print("Scalene")
class sum:
   
    def __init__(self):
        a = int(input("Enter any number for sum:- "))
        b = int(input("Enter any number for sum:- "))
        sum = a + b 
        print(f"Sum of {a} and {b} is = {sum}")
        
class sub(sum) :
    
    def  __init__(self):
          a = int(input("Enter any number for sub:- "))
          b = int(input("Enter any number for sub:- "))
          sub = a - b 
          print(f"Sub of {a} and {b} is =  {sub}")
          super().__init__()

s1 = sub()  
        
        
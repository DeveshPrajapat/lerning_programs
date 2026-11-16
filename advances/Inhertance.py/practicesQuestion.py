# class Person:
#     def __init__(self,id):
        
#         print(f"Person id is {id}")
        
# class Employee(Person):
#     def __init__(self,salary):
#         add  = int(input("Add the salay "))
#         sum = salary + add
#         print(f"sum")
        
# class Manger(Employee):
#     def __init__(self,id,salary):
#         dep = input("Add the department ")
#         super().__init__()
#         super().__init__()
#         print(f"Employee {self.id} , salary {self.sum},department {dep}")
        

# ma = Manger(1,2000)


class student:
    def display(self,name,roll_no,marks):
        print(f"Name :- {name}\nRoll No :-  {roll_no}\nMarks :- {marks}")
        if 100 >= marks >= 81:
            print(f"Student Grade is 'A'")
            print("--------------------------")
        elif 80>= marks >= 61:
            print(f"Student Grade is 'B'")
            print("--------------------------")
        elif 60>= marks >= 41:
            print(f"Student Grade is 'C'")
            print("--------------------------")
        else:
            print(f"Student is failed")
            print("--------------------------")

s = student()
s.display("devesh",39,84)
s.display("Dhruv",41,74)
s.display("Harsh",56,64)
s.display("abc",6,34)


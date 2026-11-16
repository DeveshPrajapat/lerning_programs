# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
        
#     def average(self):
#         sum = 0 
#         count = 0
#         for i in self.marks:
#             sum+=i
#             count+=1
            
#         print(f"Hi {self.name},Your Average of Marks {sum/count:.2f}")

# s = Student("devesh",[98,78,92])
# s.average()

# ! Banking systme Debit and credit 

class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account = acc
        
    def debit(self,amount):
        self.balance -= amount
        print(f"Rs {amount} , was debited")
        print(f"Total balance is {self.get_balance()}")
        
    def credit(self,amount):
        self.balance += amount
        print(f"Rs {amount} , was credit")
        print(f"Total balance is {self.get_balance()}")
    
    def get_balance(self):
        return self.balance


ac = Account(10000,1234)
ac.debit(1000)
ac.credit(500)

        
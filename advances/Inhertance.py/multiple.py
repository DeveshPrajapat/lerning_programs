class father :
    def skills(self,drwing):
        print(f"Gardening {drwing}")
class mother:
    def skills(self):
        print("Cooking")
class child(mother,father):
    def show(self):
        print("Child own talent")
        father.skills(self,"gace")
        mother.skills(self)
        
c = child()
c.skills()
c.show()
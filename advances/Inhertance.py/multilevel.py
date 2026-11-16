class Grandpa:
    def grandpa(self):
        print("This is Grandparent Class")
class Parent(Grandpa):
    def parent(self):
        print("This is Parent Class")
class child(Parent):
    def Child(self):
        print("This is Child Class")
        
ch = child()
ch.Child()
ch.parent()
ch.grandpa()
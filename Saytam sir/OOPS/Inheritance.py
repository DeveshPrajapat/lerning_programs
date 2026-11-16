class Animal():
    
    def dog():
        print("Animal make a sound")
    

class Dog(Animal):
    def bark():
        print("dog barks")
        

d = Dog
d.dog()
d.bark()
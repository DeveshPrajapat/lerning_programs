class Animal :
    def speakk(self):
        print("Animal makes a Sound ")
    
class Dog(Animal):
    def speak(self):
        print("Dog barks ")
    
ani = Dog()
ani.speak()
ani.speakk()

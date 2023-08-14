class Animal:  
    def speak(self):  
        print("Animal Speaking")
    def eat(self,animalName):
        print(f"{animalName} eat insects")  
#child class Dog inherits the base class Animal  
class Dog(Animal):  
    def bark(self):  
        print(f"barking")  
class Cat(Dog):
    def bark(self):  
        print(f"Meon")  
d = Dog()  
d.bark()  
d.eat('Dog')  
d.speak()  

c=Cat()
c.bark()
c.eat('Cat')

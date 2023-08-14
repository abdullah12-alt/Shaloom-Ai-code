# a = 5
# print(type(a))

# b= 'hello'
# print(b.capitalize())

# there two type of classes
# user define 
     
# built in/ pre define
#   int , str,bool,complex,float, list etc


# classes user define

class Human:
    color = 'white'
    def __init__(self):
        print('hello human')
    def walk(self,first,name):
        print(f'{name} can walk')
    
# shahloom = Human()    
# print(shahloom)
# print(shahloom.color)
# print(shahloom.walk('shaloom'))


class Dog:

	# class attribute
	attr1 = "mammal"

	# Instance attribute
	def __init__(self, name):
	   self.name = name
    
    
  
  
# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

Rodger.attr1='human'
print(Rodger.attr1)
print(Tommy.attr1)
# Accessing class attributes
print(f"Rodger is a {Rodger.__class__.attr1}")
print("Tommy is also a {}".format(Tommy.__class__.attr1))

# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))
print(isinstance(Rodger, Human))
# verification of object   


# Constructor :
    # we can define it with __init__  
    # we dont need to call it by it's name .it is automatically call when we create or instantiate an object
    # we define it right after the class


class Base:
    @staticmethod
    def greet(name):
        print("hello "+name)
        

obj = Base()
print(obj.greet('shaloom'))
print(obj.greet('ali'))
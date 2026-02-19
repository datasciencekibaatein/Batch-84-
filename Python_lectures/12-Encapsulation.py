#What is encapsulation
'''
Encapsulation means wrapping data and method into a single unit and restricting direct access.
'''

class Car:
    def start(self):
        print("Car is starting")


#car = Car()
#car.start()

'''
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks



    def display(self):
        print(f"My name is {self.name} and marks are {self.marks}")


s = Student("Alice",355)
'''
#s.display()

'''
name = "rohit"
marks = 45
print(f"hello {name} and marks {marks}")
print("hello ",name," and marks",marks)
'''

#Why encapsulaiton ?
'''
1. Data hiding
2. Security
3. Control over Data
4. Easy maintenance
5. Flexibility
'''


#Example without encapsulation
class Bank:
    def __init__(self):
        self.balance = 10000


dhruv = Bank()
dhruv.balance = 15000

sohit = Bank()
sohit.balance = -5000

#print(sohit.balance)


#Encapsulation
'''
- public
- protected
- private
'''

#Public

#Accessible everywhere
'''
Public member have no underscore(prefix). They are accessible from anywhere, inside the class,
subclasses, or external code, all attributes and methods are public by default
'''
class Vehicle:
    def __init__(self):
        self.carName = "LC"

v = Vehicle()
print(v.carName)



#Protected
'''
Protected members use a single underscore prefix. They are intended for internal use within
the class and its subclass but technically accessible from outside (discouraged by convention).
Use it on your own risk
'''
class Student:
    def __init__(self):
        self._marks = 90


s = Student()
print(s._marks)


#Private
'''
Private members use double underscore prefix, they are strongly restricted to class itself adn not easily 
accessible from subclasses or outside .
'''
class Employee:
    def __init__(self):
        self.__salary = 28000

    def checkSalary(self):
        print(self.__salary)


e = Employee()
e.checkSalary()
#print(e.__salary)

    
class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f"public voice of {self.name}")#public method

    def _protected_voice(self):
        print(f"protected voice of {self.name}")#protecte method
        
    def __private_voice(self):
        print(f"private voice of {self.name}")#private method


a = Animal("Lion")
a.speak()
a._protected_voice()
#a.__private_voice()

        
#class & object
#class is blueprint  or template to create object

class Car:
    num = 11
    pass

c1 = Car()
print(c1.num)
print(type(c1))

#what is an object?
'''
it is just an instance.
'''


#structure
class Classname:
    def __init__(self):
        #constructor
        pass

    def method_name(self):
        #method
        pass


#constructor is automatically called when object is created
'''
class Animal:
    ears = 2  
    def __init__(self):
        print("speaks")
        print(Animal.ears)

    def method_run():
        print("running")
    
'''

# a = Animal()


#parameterized constructor
class Student:
    def __init__(self,name,marks):
        print("intializing student")
        self.name = name #instance variable
        self.marks = marks


    def display(self):#instance
        print("Name: ",self.name)
        print("Marks: ",self.marks)


s1 = Student("Rohan",34)
s1.display()

#default parameterized constructor
class Animal:
    def __init__(self,name="pet"):
        print("initializing the animal object",name)
        self.name = name


a1 = Animal("Dog")
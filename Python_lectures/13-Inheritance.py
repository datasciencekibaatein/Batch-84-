#Inheritance
'''
Inheritance allows child class to use parents class properties
'''

'''
Animal -> Dog -> Puppy
Parents -> child
'''

# 1. Single inheritance
class Animal:#Parent class
    def __init__(self):
        print("this is parent class")
    
    def eat(self):
        print("animal is eating")

class Lion(Animal):#Child class of Animal
    def __init__(self):
        print("This is Child Class")

    def roar(self):
        print("lion in roaring")


a = Animal()
l = Lion()

#a.roar()
l.eat() # we can access the method of parent class using the child class object but parent class can not access the properties of cild class


#Why we use inheritance?
'''
- We can reuse the code again
- Less duplicate
- Easy to maintain
'''

#types of inheritance
'''
1. Single Inheritance
2. Multiple Inheritance
3. Multilevel Inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance
'''

#1. Single Inhertance (example given above)
#2.  Multiple Inheritance
'''
When child class inherits multiple parent class
'''

class Father:
    def skill(self):
        print("Driving")

class Mother:
    def skills(self):
        print("cooking")

class Child(Mother,Father):#Multiple inheritance
    pass

c = Child()
c.skills()
c.skill()


#3. Multi level inheritance
class A:
    def methodA(self):
        print("A")

class B(A):
    def methodB(self):
        print("B")

class C(B):
    def methodC(self):
        print("C")

a = A()
b = B()
c = C()

c.methodA()

#4. Hierarchical Inheritance
class Parent:
    def show(self):
        print("parent")

class Child1(Parent):
    pass

class child2(Parent):
    pass
        

#5. Hybrid Inheritance
'''
Combining all the inheritance together , we refer it hybrid inheritance
'''
#Polymorphism
#Poly = many
#morph = forms

'''
Same method name -> different behavior.
'''

#Types of polymorphism in python

'''
- Method overriding
- Method overloading
- Operator overloading
- Duck typing
'''


#method overriding(runtime polymorphism)

class Animals:
    def sound(self):
        print("Animal makes sound.")

class Dog(Animals):
    def sound(self):
        print("Dog barks")

class Cat(Animals):
    def sound(self):
        print("Cat meows")


'''
animals = [Dog(),Cat(),Dog()]
for a in animals:
    a.sound()
'''


print(5 + 3)
print("hello "+"jhgf")

#operator overloading
class Vector:
    def __init__(self,x):
        self.x = x

    def __add__(self,other):
        return Vector(self.x + other.x)#vector(20+10)
    
    def __str__(self):
        return f"vector({self.x})"
    
v1 = Vector("hjk")
v2 = Vector(" gvfkm")

# print(v1+v2)

# print(v1.__add__(v2))


class Calculator:

    def add(self,a,b,c=0):
        return a+b+c
    
calc = Calculator()
# print(calc.add(2,3))
# print(calc.add(2,2,3))


#Duck Typing
class JupyterNotebook:
    def execute(self):
        print("Running python code")

class VSCode:
    def execute(self):
        print("Running python script")

def run_environment(env):
    env.execute()


jn = JupyterNotebook()
vs = VSCode()
run_environment(jn)
run_environment(VSCode())

#Python does not care about object type.
#It cares whether mehod exists or not

print(type(vs))
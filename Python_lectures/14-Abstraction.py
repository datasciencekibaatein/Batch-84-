#Abstraction
'''
Abstraction means hiding implementation details and showing only essential features to the user.
'''
# User ko sirf 'what to use' pata hona chahiye
# 'how it works' nhi pata hona chahiye

#Example
'''
ATM Machine
Car driving
Mobile
'''

#Why Abstraction is important?
'''
- Reduce complexity
- Improves security
- Makes code reusable
- Makes system scalable
- Separate interface from implementation
'''


#How to achieve abstraction in python ?
'''
1. Abstract base class (ABC)
2. @abstractmethod decorator
3. abc module
'''


#Syntax
'''

from abc import ABC,abstractmethod

class Parent(ABC):

    @abstractmethod
    def method_name(self):
        pass
'''

from abc import ABC,abstractmethod
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car is starting with key.")

    
class Bike(Vehicle):
    def start(self):
        print("bike start with self-start button")

'''
c = Car()
c.start()

b = Bike()
b.start()

v = Vehicle()
v.start() # You can not create object o vehicle class, because abstart class cannot be instantiated.
'''


#Payment system

from abc import ABC,abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self,amount):
        pass

class CreditCardPayment(Payment):

    def pay(self,amount):
        print(f"Paid {amount} using credit card.")
        
    
class UpiPayment(Payment):
    
    def pay(self,amount):
        print(f"Paid {amount} using UPI.")

class NetBankingPayment(Payment):
    def pay(self,amount):
        print(f"Paid {amount} using net banking.")




def make_payment(payment_method,amount):
    payment_method.pay(amount)


make_payment(CreditCardPayment(),1000)
make_payment(UpiPayment(),670)







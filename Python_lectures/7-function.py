#User defined function
#buit in function i.e print,len, input, int()
#annonymous function
'''

def checkEvenOdd(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")
'''
        
        
# checkEvenOdd(5)
# checkEvenOdd(4)
# checkEvenOdd(7)

'''

def greet():#function definition
    print("Hello, this is first function")


greet() # function call

greet()
'''

'''
#Function with parameter
def greet(name):#'name' is parameter
    print("hello ",name)



greet("Rohit")#passing argument
'''



#function with return statement
'''
def add(num1,num2):
    print("num1 is: ",num1,"num2 is: ",num2)
    return num1+num2


print(add(34,56))
'''



#Default argument
'''
def greet(name = "Guest"):
    return print("hello "+name)


greet("Alice")
'''


#Keyword Arguments
'''
def student(name, age):
    return print("Age of",name,"is",age)



student(age=21,name="Krish")
'''


#Arbitrary Arguments 
'''

def add_numbers(*args):
    total = 0
    for num in args:
        total+=num
    return print(total)

add_numbers(45,56,67,89,67,90)
'''


#Keyword arbitrary argument(**kwargs)
'''
def details(**kwargs):
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key,":",value)
        
    
details(name="Alice",age=24,city='mumbai')
'''


#local & global variable
'''
y = 30 #global scope
def test():
    print(y)
    x = 10 #local scope
    print(x)
    
test()
# print(x)
'''




#modify a global variable inside function
'''
x=10

def change():
    global x # modifying to global
    x = 20
    
change()
print(x)
'''




#nested functions
'''
def outer():
    print("Outer function")

    def inner():
        print("This is inner function")
    
    inner()
    
outer()
'''



#lambda function(Anonymous function)
'''
res = lambda num1,num2:num1+num2

print(res(34,78))
'''


#function documnetation

def add(num1,num2):
    '''
    Docstring for add
    
    :param num1: first argument
    :param num2: second argument
    '''
    return num1 + num2

# print(add.__doc__)

# print(print.__doc__)


# print(len.__doc__)
# print(type.__doc__)


# Recursive function
#4 => 4x3x2x1


def fact(n):
    if n==0:
        return 1
    
    return n*fact(n-1)


print(fact(5))



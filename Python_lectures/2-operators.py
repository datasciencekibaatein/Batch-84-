# Operators
# Operators are the symbols , those help us to perform operation



# Arithmetic operators (+,-,*,/,//,%,**)
# Assignment operators (=)
# Comparision operators (==,!=, >,<,>=,<=)
# Logical Operators (and, or, not)
# Bitwise Operators (&,|,~,^,<<,>>)
# Membership Operators (in, not in)
# Identity Operators (is , is not)


# arithmetic operators
num1 = 12
num2 = 12
'''
print(num1 + num2 )

print(num1 - num2)

print(num1*num2)

print(num2/num1)
print(num2//num1)

print(num2%num1)

print(num2 ** 2)
'''

# Comparision Operators
# Comparision operators return True or false based on Comparision
num1 = 12
num2 = 10
'''
print(num1 == num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)
print(num1 != num2)
'''

# Logical operators
salary = 45000
age = 17

'''
T AND T = T
T AND F = F
F AND T = F
F AND F = F
'''

# print((salary > 40000) and (age >=18))
'''
T OR T = T
T OR F = T
F OR T = T
F OR F = F
'''
# print((salary > 40000) or (age >=18))

'''
T = F
F = T
'''

# print(not(salary < 40000))

# print(not(False))

# Bitwise operators

'''
T AND T = T
T AND F = F
F AND T = F
F AND F = F
'''

'''
T XOR T = F
T XOR F = T
F XOR T = T
F XOR F = F
'''

#1010 = 10
#1100 = 12
#1000 = 8 & operation
#1110 = 14 | operation
#0110 =  6 ^ OPERATION
101000
# 1010 -> 0000
# not , ~x = -(x+1)
'''
print( 10 & 12)
print( 10 | 12)
print(~12)
print(10 ^ 12)
print(10<<2)
print(10>>4)
'''


#Assignment Operators (you can combine all the assignment and bitwise operators with them)
num = 12 #1100
print(num)

num|=4


# print(num)



# Identity operators
lst = [34,42,64]
lt = lst


# print(lst)
# print(lt)


# print(lst is lt)


# membership operators

lst = [34,42,64]

print(35 in lst)
# map
'''
Applies a function to each element of an iterable(collection)
'''

# def sqr(n):
#     return n**2

numbers = [1,2,3,4,5,6,7]
# print(list(map(sqr,numbers)))

# print(list(map(lambda y:y**2,numbers)))

names = ["dhruv","data","science"]
# print(list(map(lambda x:x.upper(),names)))



#filter function
#Filter elements based on condition

def even(n):
    return n%2==0


# print(even(5))
'''
print(list(filter(even,numbers)))
print(list(filter(lambda x:x%2==0,numbers)))

'''
# if number greater than 5
'''
print(tuple(filter(lambda c:c>5,numbers)))

'''

lst = [12,23,21,4,5,32]
#square the even number
'''
print(list(map(lambda y:y**2,
    filter(lambda x:x%2==0,lst))))
'''

#reduce
from functools import reduce


# it reduces an iterable to a single value by repeatedly applying function

#reduct(function,iterable)

# sum of elements of iterable

# print(reduce(lambda x,y:x+y,numbers))

# step 1 : 1 + 2 = 3
# step 2 : 3 + 3 = 6
# step 3 : 6 + 4 = 10
# step 4 : 10 + 5 = 15
# step 5 : 15 + 6 = 21
# step 6 : 21 + 7 = 28


# initial value of x 
# step 0 : 0 + 1 = 1
# step 1 : 1 + 2 = 3
# step 2 : (1 + 2) + 3 = 6
# step 3 : ((1 + 2) + 3) + 4 = 10
# step 4 : (((1 + 2) + 3) + 4) + 5 = 15
# step 5 : ((((1 + 2) + 3) + 4) + 5) + 6 = 21
# step 6 : (((((1 + 2) + 3) + 4) + 5) + 6) + 7 = 28


# print(reduce(lambda x,y:x+ " " + y,names))

# to find longest string in list

print(reduce(lambda x,y:x if len(x)>len(y) else y,names))

# count total characters in list

print(reduce(lambda x,y: x + len(y),names,0))
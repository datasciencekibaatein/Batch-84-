#map 
lst = [3,4,5,2,5,6]

def sqr(n):
    return n**2

print(list(map(sqr,lst)))

#map(function,iterable)

print(list(map(lambda x:x+2,lst)))


#Filter function

def grtr(n):
    return n>3

print(list(filter(grtr,lst)))


print(list(filter(lambda x:x>3,lst)))



#reduce
from functools import reduce
nums = [2,3,4,2,5,6]
total = 0
for n in nums:
    total+=n

print(total)


result = reduce(lambda x,y:x+y,nums)
print(result)
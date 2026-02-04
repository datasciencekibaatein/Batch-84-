
'''
# list, tuple, set, dictionary

# mutable , we can put duplicate element, we access data in order
lst = [31,23,65,34,26]
print(lst)
lst.append(56)
print(lst)



#tuple 
# it is immutable, allows duplicate, we access data in order
tp = (10,23,56,87,34)
print(tp[0])


#set 
# unordered , mutable collection of unique values
numbers = {1,3,4,67,5,3,6}
names ={"sohit","sohit","krish"}
print(names)
print(numbers)


#Dictionary

# It is key-values pairs, unordered (ordered from puthon 3.7+)

students = {
    "name":["Rohan","Krish","Amit","Prakash"],
    "age":[22,23,21,25],
    "course":["math","python","dbms","networking"],
}
print(students["name"][1],students["age"][1],students["course"][1])

print(students.keys(),students.values())

'''



#list functions
'''
lst = [4,6,3,9,4]
print(lst)
lst.append(7) # append at the end of list
print(lst)
lst.insert(1,34) # insert element at any specific index
print(lst)
lst.remove(4)
print(lst) #it removes the first occurence of element 
print(lst.pop()) # pop without parameter removes & return the last element from list
print(lst)
print(lst.pop(3)) # pop element by passing index
print(lst)
lst.sort() # after this functino it will give you sorted list
print(lst)
print(lst.index(6)) # it returns the index of element
print(lst.count(4)) # it returns the count of occurence of element in list
lst.clear() # it removes all the element from list , and return empty list
print(lst)
'''

# tuple functions
'''
tp = (34,67,89,23,23)
print(tp.count(23)) # count the occurence of the element
print(tp.index(23))
'''

# set functions
'''
numbers = {1,2,3,4}
print(numbers)
numbers.add(5) # add number in set , if it already exist the you will get single element only 
print(numbers)
numbers.remove(4) # It removes element, if number does not exists it will give you error
print(numbers)
numbers.discard(6) # it removes element if exists , if not , it will not give error
print(numbers)
numbers.pop() # it remove random element from set
print(numbers)

#set operations Union, intersection, difference

a = {1,2,3,4}
b = {4,5,1,6}

print(a.union(b)) # It combines the sets together
print(a.intersection(b)) # it reflect common element from sets
print(b.difference(a)) # elements in one set only 

'''

'''
student = {
    "name":"Alice",
    "age":21,
    "course":"DSA"
}

print(student.keys())
print(student.values())
print(student.items()) # here you will  get key-values pair
print(student.get("age")) # get value of any key
print(student.update({"course":"Networking"})) # you can update or add key - value pair
print(student.update({"city":"Rio"}))
print(student)
print(student.pop("age")) # remove pair by using key
student.clear()
print(student)
'''



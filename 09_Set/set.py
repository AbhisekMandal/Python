#set 
#A set is a collection which is unordered, unchangeable*, and unindexed.
#Note: Set items are unchangeable, but you can remove items and add new items.
# thisset = {"apple", "banana", "cherry"}
# print(thisset)

# #Set items are unordered, unchangeable, and do not allow duplicate values.
# thisset = {"apple", "banana", "cherry", "apple"}
# print(thisset) #Duplicate values will be ignored:
# #Set DataType ==> <class 'set'>
# set1 = {"apple", "banana", "cherry"}
# set2 = {1, 5, 7, 9, 3}
# set3 = {True, False, False}
# print(type(set1))
# print(type(set2))
# print(type(set3))

# #Access Set : using loop
# for x in thisset:
#     print(x)

# #Add item using ==> add()
# thisset.add("Orange")

# # update() ==> add more than one value
# numbers = {1,2,3,3,4,5,6,6}
# thisset.update(numbers)
# for x in thisset:
#     print(x)

# # Remove items ==> remove() or discard()
# numbers.remove(3)
# # numbers.discard(6)
# for x in numbers:
#     print(x)
# #You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
# numbers.pop()
# print(numbers)
# #The clear() method empties the set:
# numbers.clear()
# print(numbers)
# #The del keyword will delete the set completely:
# del numbers
#print(numbers) #NameError: name 'numbers' is not defined. Did you forget to import 'numbers'?

#IMPORTANT 
#Join sets: union(), update(), intersection(), difference(), symmetric_difference()
#==========

#The union() and update() methods joins all items from both sets.
set1 = {"a","b","c",10,20,30,40}
set2 = {"c","d","e",30,40,50,60}
set3 = set1.union(set2) #You can use the | operator instead of the union() method, and you will get the same result.
set4 = set1 | set2
print(set3)
print(set4)
#The intersection() method will return a new set, that only contains the items that are present in both sets.
set3 = set1.intersection(set2)
print(set3)
#You can use the & operator instead of the intersection() method, and you will get the same result.
set3 = set1 & set2
print(set3)

#Lists are used to store multiple items in a single variable.
#Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
#Lists are created using square brackets:

mylist = ["apple","banana","coconut","orange"]
print(mylist)
print("Length of mylist:", len(mylist))

#list can be any data type
anyList = [2,"KGF",True]
print(anyList)

#data type of list is <class 'list'>
print(type(anyList))

#Using the list() constructor to make a List:
fruits  = list(("apple","Coconut"))
print(fruits)

#List is a collection which is ordered and changeable. Allows duplicate members.

#append() : add element at the ende of the list
fruits.append("orange")
print(fruits)

#insert() : add item in a specific index
fruits.insert(1,"mango")
print(fruits)

#To append elements from another list to the current list, use the extend() method.
bikes = ["Truimp","BMW","Suzuki"]
fruits.extend(bikes)
print(fruits)

#The remove() method removes the specified item.
fruits.remove("Suzuki")
print(fruits)

#The pop() method removes the specified index.
fruits.pop(1)
print(fruits)

#The clear() method empties the list.
fruits.clear()
print(fruits)

#ist objects have a sort() method that will sort the list alphanumerically, ascending, by default:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana","apple"]
numlist = [25,13,45,80,40,8,5,2]
thislist.sort()
numlist.sort()
print(thislist)
print(numlist)

#Descending order
numlist.sort(reverse = True) 
print(numlist)
thislist.reverse()
print(thislist)

#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	    Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	    Removes the element at the specified position
#remove()	Removes the item with the specified value
#reverse()	Reverses the order of the list
#sort()	    Sorts the list

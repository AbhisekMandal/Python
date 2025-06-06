#Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
#A tuple is a collection which is ordered and unchangeable. We can't add or remove element.
#Tuples are written with round brackets.
firstTuple = ('lion','tiger','crocodole')
print(type(firstTuple)) #<class 'tuple'>
print(firstTuple)
testTuple1 = ('lion')
print(type(testTuple1))#<class 'str'>
testTuple2 = ('lion',)
print(type(testTuple2)) #<class 'tuple'>

#Access Tuple items
EvenNum = (2,4,6,8,10,12,14,16,18,20)
print(EvenNum[2])
print(EvenNum[0])
# -1 refers to the last item, -2 refers to the second last item etc.
print(EvenNum[-1])
print(EvenNum[-2]) 

#Range of Index
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#Update Tuples
#Convert the tuple into a list to be able to change it:
thisList = list(thistuple)
thisList[1] = "coconut"
thisList[2] = "lichi"
print(thisList) #['apple', 'coconut', 'lichi', 'orange', 'kiwi', 'melon', 'mango']
print(thistuple) #('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')
#converting list to tuple
thistuple = tuple(thisList)
print(thistuple) #('apple', 'coconut', 'lichi', 'orange', 'kiwi', 'melon', 'mango')

#unpacking tuple
#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
(green, yellow, *red) = thistuple
print(green) #apple
print(yellow) #banana
print(red) #['cherry', 'orange', 'kiwi', 'melon', 'mango']
(green, *yellow, red) = thistuple
print(green) #apple
print(yellow) #['banana', 'cherry', 'orange', 'kiwi', 'melon']
print(red) #mango

#loop in tuple
for x in thistuple:
    print(x)

# loop through index
for i in range(len(thistuple)):
    print("Index",i,":",thistuple[i])

#join two tuple
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
#Multiply the fruits tuple by 2:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
#count() :The count() method returns the number of times a specified value appears in the tuple.
print(mytuple.count("apple"))
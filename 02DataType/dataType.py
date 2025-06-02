# Data Types in python
#Getting data type of a variable we use 'type()' function

# Text type ==> str
name = 'Abhisek'
print(type(name)) # <class 'str'>

# Numeric Type ==> int, float, complex
age = 25
salary = 12000.56
x = 2j
print(type(age)) # <class 'int'>
print(type(salary)) # <class 'float'>
print(type(x)) #<class 'complex'>

# Sequence Types ==> list, tuple, range
fruits = ['mango','apple','orange']
bikes =('Truimp ','Scrambul 400','GT450')
y = range(6)
print(type(fruits)) # <class 'list'>
print(type(bikes)) # <class 'tuples'>
print(type(y)) #<class 'range'>

# Mapping Type ==> dict
details = {"name": "Basanta", "age":36}
print(type(details))#<class 'dict'>

#Set Types ==> set, frozenset
cars = {"BMW","VW","Mahindra"}
movies = frozenset({"KGF","Kantara","Puspa"}) # we can not the edit 'frozenset({})'
print(type(cars)) #<class 'set'>
print(type(movies))  #<class 'frozenset'>


#Boolean Type ==> bool
z = True
print(type(z))  #<class 'bool'>

#Binary Types ==> bytes, bytearray, memoryview
a = b"hello world"
b = bytearray(6)
c = memoryview(bytes(6))
print(type(a)) #<class 'bytes'>
print(type(b)) #<class 'bytearray'>
print(type(c)) #<class 'memoryview'>

#None Type ==> NoneType
d = None
print(type(d))


#String is a collection of characters 
print("hello")
print('hello')

print("I am from 'Odisha',")
print('My name is "Abhisek"')

#Assign string to a variable
a = "Nike"
print(a)

#Multiline Strings
#You can assign a multiline string to a variable by using three quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#To get a perticular character 
a = 'Hello world!'
print(a[0]) # H

#Slicing String : By using this you can get a renage of characters
b ="I am Abhisek"
print(b[2:10])

#Modify String
#==============

#Upper Case --> upper()
a = "hello world!"
print(a.upper())

#Lower Case --> lower()
b="  HELLO WORLD!  "
print(b.lower())

# Remove space -->strip()
print(b.strip())

#Replace --> replace(): method replace a string replace with another string
print(a.replace("h","J")) #Jello world!

#split()--> method used to split the string in a list
print(a.split(" ")) #['hello', 'world!']

#String Concatanation
#=====================
a = "Hello!"
b = " I am Abhisek"
c = "from Odisha"
print(a+b+c) #Hello! I am Abhisekfrom Odisha
print(a,b,c) # Hello!  I am Abhisek from Odisha. Note: By default it will take white space

#String Method
#==============
name = "Basanta Mandal"
location = "bhubaneswar, odisha"

#capitalize() ==> Converts the first character to upper case
print(location.capitalize()) #Capitalize the fisrt letter of the sentence

#swapcase() ==> Swaps cases, lower case becomes upper case and vice versa
print(name.swapcase())



 
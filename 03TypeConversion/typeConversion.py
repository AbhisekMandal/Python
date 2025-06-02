# In some scenario we need to assign perticural datatype type
name = str('Abhisek')
age = int(25)

# Type Convertion : converting one datatype to another datatype
x = 1 
y = 25.65
z = 25j
print(x , type(x))
print(y , type(y))
print(z , type(z))

print("After Type Conversion")
a = float(x)
b = int(y)
c = complex(x) # We can convert 'int' to 'complex' but not 'complex' to 'int'
print(a , type(a))
print(b , type(b))
print(c , type(c))
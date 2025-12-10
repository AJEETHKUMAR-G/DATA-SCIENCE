                                 #EVERY PRO WAS ONCE A BEGINNER
#1. BASIC DATA TYPES
#TEXT TYPE: (STRING)
a = "Aju"
print(a)
print(type(a)) #"type()" is used to check the data type of given variable
# we can use either "" or '' to represent a string

print("**********************************************")

b = 'ronaldo'
print( "the value stored in the variable is of" ,type(b),"category")
print(b)

print("**********************************************")
print("********************************************** \n")

#NUMERICAL TYPE:

#INTEGER:
a = 3
b = 6483932930
c = -2327346347
print(a)
print( "the value stored in the variable is of" ,type(a),"category \n")

print(b)
print( "the value stored in the variable is of" ,type(b),"category \n")

print(c)
print( "the value stored in the variable is of" ,type(c),"category \n")

print("**********************************************")

#COMPLEX:

b = 8j + 567
c = 45 + 0j
d = 5j
print(b)
print( "the value stored in the variable is of" ,type(b),"category \n")
print(c)
print( "the value stored in the variable is of" ,type(c),"category \n")
print(d)
print( "the value stored in the variable is of" ,type(d),"category \n")
print("**********************************************")

#FLOAT:

c = 3.456
e = -23.23236
print(c)
print( "the value stored in the variable is of" ,type(c),"category \n")
print(e)
print( "the value stored in the variable is of" ,type(e),"category \n")
print("**********************************************")
print("********************************************** \n")

#2. CASTING

a = int(2.3455)
print(a,type(a))
b = int("78")#A Double quote containg only whole numbers can be an "integer"
print(b,type(b))
"""
a = int("2.3455") A Double quote containg Floating values can't be an "integer"
b = int(3j) A complex number can't be an "Integer"
c = int("s") A Double quote containg letters can't be an "integer"
print(a,type(a))     Printing it's type will raise an value error
print(type(b))       Printing it's type will raise an value error
print(type(c))       Printing it's type will raise an value error"""
x = complex(3)
print(x,type(x))
y = complex(3.98)
print(y,type(y))
z = complex("3.9887")
print(z,type(z))
w = complex("34")
print(w,type(w))
"""c = complex("s")   A Double quote containg letters can't be a "complex "
print(type(c))        Printing it's type will raise an value error """
x = float(3)
print(x,type(x))
y = float("87")
print(y,type(y))
"""z = float(3j) arguement passed is not valid so it will raise type error
print(z,type(z))
y = float("d")
print(y,type(y)) Value error"""
x = str(3)
print(x,type(x))
x = str(3j)
print(x,type(x))
y = str(3.98)
print(y,type(y))
z = str("3.9887")
print(z,type(z))
w = str("34")
print(w,type(w))
print("**********************************************")
print("********************************************** \n")

#BOOLEAN:

x = True # "T" must be in uppercase
print("The given variable is of", type(x),"category")
y = False# "F" must be in uppercase
print("The given variable is of", type(y),"category")
print("**********************************************")
print("********************************************** \n")

#SOME OTHERS TO KNOW:

#SET: #VALUES STORED INSIDE SET BRACKETS

a = {"34","neymar",3j,7}
print("The given variable is of", type(a),"category")
a = ({"34","neymar",3j,7}) 
print("The given variable is of", type(a),"category")



#FROZENSETS:

a = frozenset({"34","neymar",3j,7}) 
print("The given variable is of", type(a),"category")

"""a = frozenset({"34","neymar",3j,7},7) this line raise error because the value is printed outside {}
print("The given variable is of", type(a),"category")"""



























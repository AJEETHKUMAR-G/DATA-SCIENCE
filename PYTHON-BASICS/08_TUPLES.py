# 6. TUPLES

#IMMUTABLE AND ALLOWS DUPLICATES
# () or tuple(())

a = (1,2,3,"Cr","Njr","r9",1,2)
print(a, type(a))

# Tuple containing one element:

b = ("aju",)
print(b, type(b))
c = ("ronaldo") # this is not considered as a tuple
print(c, type(c))

d = tuple((12,"hattori",True,"shinso"))
print(d,type(d))

# ACCESSING ELEMENTS:

k = (1,2,3,"Cr","Njr","r9",1,2)
print(len(k))
print(k[3])
print(k[-2])
print(k[1:6])  # similar slicing concepts

print(2 in k)

# UPDATE TUPLE
#We can't change the elements of tuple instead we change that tuple as a list
#and change that list to tuple

x = ("cr","lm",23)
y = list(x)
y[1] = "njr"
x = tuple(y)
print(x)

# Appending:

x = ("cr","lm",23)
y = list(x)
y.append(237)
x = tuple(y)
print(x)

# tuple + tuple

x = ("cr","lm",23)
y = ("eh",)
z = ("njr","km")
print(x+y+z)

# remove :
v = list(x)
v.remove(23)
b = tuple(v)
print(b)

#del y  --> raise error 
#print(y)

# UNPACKING:

a = ("cr","aj","rd") # packing
(a,b,c) = a # unpacking
print(a)
print(b)
print(c)

# if variable is lesser than value, we use"*"

a = ("cr","aj","rd",1,23,4546) # packing
(a,b,*c) = a # unpacking
print(a)
print(b)
print(c)

a = ("cr","aj","rd",1,23,4546) # packing
(a,*b,c) = a # unpacking
print(a)
print(b)
print(c)

v = a.count("235")
print(v)
a = (12,23,"aju")
c = a.index(12)
print(c)























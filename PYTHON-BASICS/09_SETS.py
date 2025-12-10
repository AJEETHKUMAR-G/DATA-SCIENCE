#7. SETS

# Unordered, Unchangeable(we can add or remove items), Unindexed
# {} or set(())
# No duplicates

a = {1,2,3,"aju","dev",0.346,"dev"}
c = set((1,2,3,"hukum","kavalaa"))
print(a,type(a))
print(len(a))
print(c,type(c),len(c))

b = {1,0,True,False}
print(b , len(b), type(b))
print(1 in b)

# ADDING ELEMENTS:
# To add one element in to a set --> add()
# To add items from another set into the a set --> update(),union()

a = {1,2,3,"aju","dev",0.346,"dev"}
a.add("sheela ki jawani")
print(a)
b = {"tum hi ho","phir kabhi","kun tujhe"}
a.update(b)
print(a)
c = [1,3,456]
b.update(c) 
o = a.union(b)
print(b)
print(o)
x = {1,2,"aju","kio"}
y = {"kio","sisimaaru",1}
x.intersection_update(y)# no new set get formed
print(x)
print(x.intersection(y)) # returns new set
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}
x.symmetric_difference_update(y)# no new set get formed
z = x.symmetric_difference(y)# returns new set
print(x)
print(z)

#d = (1,234) c.update(d) raise attribute error


# REMOVE ITEMS

a = {1,2,3,"aju","dev",0.346,"dev"}
a.remove(1)#if the item does'nt exist it will raise error
print(a)
a.discard("dev")#if the item does'nt exist it won't raise errors
print(a)
w = a.pop()# we don't know which item got removed
print(a)
print(w)
a.clear()
print(a)
"""del b
print(b)"""

# SOME OTHERS:

a = {"aju","cr","dev","njr"}
x = a.copy()
print(x)
b = {"aju",23,12}
y = a.difference(b)# returns new set
print(y)
x.difference_update(b)# no new sets
print(x)
f = {"aju",23,12,"njr"}
print(x.issubset(b))
print(b.issubset(f))
print(b.issuperset(f))
print(f.issuperset(b))
c = {1,2}
print(x.isdisjoint(c))































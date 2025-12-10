#LISTS
# SEQUENTIAL DATA TYPE
# List are used to store multiple values in a single variable
# Mutable and allows duplicate
# Represent by "[]" or "list(())"

a = ["aju","ronaldo","mbappe","haaland","bale","ramos",71,7,10,18,9,10]
b = list(("messi","suarez","neymar","martinez","dybala","mane"))
print(b)
print(a)
print(type(a))
print(type(b))
print(len(a),len(b))
print(a[3])
print(b[0:5])
print(a[-6])
print(b[-1:-4:-1])
print(a[-2:-6:-2])
print(a[::-1])
print(b[::])
a.append("marcelo")# adds the element at the last index
print(a)
b.insert(0,"ronaldinho")# arg1 = index where the value wants to get insert,arg2 = element
print(b)
a.insert(0,b) # inserting ""list"" b in the 0th index of list a
print(a)
print(a[0])
a.extend(b) # adds ""list values"" of b at the last of list a
print(a)

d = ["aju","ronaldo","mbappe","haaland","bale","ramos"]
d.remove("aju")
print(d)
print(d.pop())
print(d)
print(d.pop(2))
print(d)
x  = list(("messi","suarez","neymar","martinez","dybala","mane"))
y = [23,1,4,76,90,0]
x.reverse()
print(x)
y.reverse() # Reverse the original list
print(y)
x.sort() #sort the original list
print(x)
y.sort()
print(y)
x.sort(reverse = True) # reverse the original list
print(x)
y.sort(reverse = True)
print(y)
u = ["k","kr","rt","ba"]
j = sorted(u) # a copy of sorted original list but it does'nt affect the original
print(j)
print(u)
print(min(u))
print(max(u))
#print(sum(u)) "sum() doesn't works for lists having strings"
i = [23,1,345,6,100,21]
print(min(i))
print(max(i))
print(sum(i))
print(i.index(100))
#print(i.index(8)) raise value error
print(1 in i)
print(11 in i)
print("**************************************")
for y in i:
    print(y)
print("**************************************")
for o,y in enumerate(i):
    print(o,y)
print("**************************************")
for o,y in enumerate(i, start = 1):
    print(o,y)
print("**************************************")

u = ["k","kr","rt","ba"]
new = " , ".join(u) # list to string
lists = new.split(",") # string to list
print(new)
print(lists)


















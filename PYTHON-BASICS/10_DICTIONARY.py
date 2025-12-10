  #8. DICTIONARY

# Ordered, Changeable, not allow duplicates
# {key: value} or dict()

a = {"name": "aju", "age": 21, "course": ["math", "mca"]}
print(a, type(a))
print(a["name"])
print(a["course"])
#print(a["class"]) raise key error because the key does'nt exist
print(a.get("age"))
print(a.get("class")) # shows none
print(a.get(1,"illa pa thambi")) # instead to show none we use 2nd arg
a["r.no"] = 64
print(a)
a["name"] = "ajeeth"
print(a)
a.update({"name": "23mca1", 20: 233, "m.no":555555})
print(a)
v = a.pop(20)
print(a)
print(v)
c = a.popitem()# removes last inserted item
print(c)
print(a)
del a["r.no"]
print(a)
# del a and a.clear() erases whole dictionary
print(len(a))
print(a.keys())
print(a.values())
print(a.items())

for a,b in a.items():  #a.keys(),a.values()
    print(a,b)






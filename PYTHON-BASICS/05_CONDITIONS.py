

# COMPARISIONS: ==, >, <, >=, <=, !=, is
# BOOLEANS: and, or, not
# MEMBERSHIP : in , not in
# IDENTITY: is, is not

print(2 > 0)
print(22 > 300)
print(2 < 0)
print(2 >= 10)
print(20 >= 0)
print(21 <= 0)
print(10 <= 20)
print(2 != 0)
print(1 == 0)

print("Hii" == "hii")
print(True == 1)
print("*************************\n")
# else part is not compulsory when using if
# if part is compulsory while using else

if True:
    print("idhu work aagum guys")


if False:
    print("varata maame")
else:
    print("pika pika")

food = "poratta"
if food == "poratta":
    print("enaku venummmm")
else:
    print("naa sapda maate...poratta dha venu")

food = "poori"
if food == "poratta":
    print("enaku venummmm")
else:
    print("naa sapda maate...poratta dha venu")

food = "noodles"
if food == "poratta":
    print("enaku venummmm")
elif food == "noodles":
    print("parava illa...chicken noodles ilaya..")
else:
    print("naa sapda maate...poratta dha venu")

food = "chicken noodles"
if food == "poratta":
    print("enaku venummmm")
elif food == "noodles":
    print("parava illa...chicken noodles ilaya..")
elif food == "chicken noodles":
    print("double ok... enaku idhu podhum")
else:
    print("naa sapda maate...poratta dha venu")


menu = ["poratta","chicken noodles","fried rice","set dosa"]
print("waiter: sir enna venum")
appa = input("")
print(appa, "irukaa pa")
if appa in menu:
    print("waiter: Aah iruku sir parcel potruvom")
else:
    print("sorry sir gaali aagiduchu vera edhachu venuma")
    opt = input("")
    print(opt,"iruka paa")
    if opt in menu:
        print("iruku sir parcel potruvom")
    else:
        print("sorry sir adhuvum illa")


menu = ["poratta","chicken noodles","fried rice","set dosa"]
print("waiter: sir enna venum")
appa = input("")
if appa in menu:
    print("iruku sir")
    if appa == "poratta":
        print("waiter: ethana sir venum")
        num = int(input())
        print(num, "venum pa")
        print("waiter:", num * 12, "rupaya bill pay panunga sir parcel vandhrum")
    elif appa == "set dosa":
        print("waiter: ethana set sir venum")
        num = int(input())
        print(num, "venum pa")
        print("waiter:", num * 35, "rupaya bill pay panunga sir parcel vandhrum")
    elif appa == "fried rice":
        print("waiter: ethana sir venum")
        num = int(input())
        print(num, "venum pa")
        print("waiter:", num * 100, "rupaya bill pay panunga sir parcel vandhrum")
    else:
        print("chicken noodles ethana sir parcel podanum")
        num = int(input())
        print(num, "venum pa")
        print("waiter:", num * 120, "rupaya bill pay panunga sir parcel vandhrum")
else:
    print("sorry sir illa..")

a = int(input("enter the number:"))
if a == 45 and a>45:
    print("nee pass da")
else:
    print("next time da")


a = int(input("enter the number:"))
if a == 45 or a>45:
    print("nee pass da")
else:
    print("next time da")


a = int(input("enter the number:"))
if not a<=45:
    print("nee pass da")
else:
    print("next time da")


a = [1,23]
b = [1,23]

if a == b :
    print("identity lists")


a = [1,23]
b = [1,23]
# here it is false because of id's have different memory locations
if a is b :
    print("identity lists")
else:
    print("false")

print(id(a))
print(id(b))


a = [1,23]
b = a
if a is b :
    print("identity lists")
else:
    print("false")

print(id(a))
print(id(b))
"""

# FALSE VALUES:

a = False

if a:
    print("idhula condition check agadhu")
else:
    print("False, 0, None nu kudutha direct aah else block dhaan")

b = None

if b:
    print("idhula condition check agadhu")
else:
    print("False, 0, None nu kudutha direct aah else block dhaan")

c = 0

if c:
    print("idhula condition check agadhu")
else:
    print("False, 0, None nu kudutha direct aah else block dhaan")


d = [] #'',{},()

if d:
    print("idhula condition check agadhu")
else:
    print("empty lists,tuple,dicts nu kudutha direct aah else block dhaan")



d = [123] #'',{},()

if d:
    print("idhula condition check agum")
else:
    print("empty lists,tuple,dicts nu kudutha direct aah else block dhaan")































    
              









    


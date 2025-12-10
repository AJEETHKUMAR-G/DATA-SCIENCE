# VARIABLES FOLLOW LEGB RULE
# 1. LOCAL 2. ENCLOSING 3. GLOBAL 4. BUILT IN 
'''
x = 'global out side the function '
def funk():
    x = 'PREPARE YOUR MINDSET'
    print(x)
funk()
print(x)
print('*****************************************')
'''
'''
global y
y = 'PREPARE YOUR MINDSET'
def funk():
    
    print(y)
funk()
print(y)
print('*****************************************')
'''
'''
def fun():
    global v
    v = 77
    print(v)
fun()
v = 90
print(v) # BY LINE BY LINE INTERPRETING IT SHOWS 90
print('*****************************************')
'''
'''
def fun():
    global t
    t = 77
    print(t)
fun()
print(t) # BY LINE BY LINE INTERPRETING IT SHOWS 77

print('*****************************************')
'''
'''
def fun():
    
    h = 77
    print(v)
    print(h)
fun()
'''
#print(v) # BY LINE BY LINE INTERPRETING IT SHOWS 90
# SHOWS NAME ERROR BECAUSE IT IS OUT OF LOCAL VARIABLE DECLARED
'''
def rre(d):
    f = 'wake up'
    print(d)
rre('5.am')
#print(d) NAMEERROR OCCUR

#import builtins
#print(dir(builtins))'''
'''
def min():
    pass
a =  min([1,2,89,0]) # SHOWS ERROR BECAUSE min() FUNC HAS 0 ARGS
print(a)
def S_min():
    pass
a =  min([1,2,89,0]) #
print(a)'''
'''
# ENCLOSING
def outer():
    x = 'wake up'
    def inner():
        x ='discipline'
        print(x)
    inner()
    print(x)
outer()'''
'''
def outt():
    c = 'getup'
    def inn():
        print(c)
    inn()
    print(c)
outt()'''
'''
def outt():
    #c = 'getup'
    def inn():
        b = 'subconcious mind powers'
        print(b)
    inn()
    print(b) # ENCLOSING SCOPE SHOWS NAME ERROR
outt()'''
'''
def outt():
    p = 90
    def inn():
        nonlocal p # SAYS THAT P IS NOT LOCAL 
        #p = 'discipline'
        print(p)
    inn()
    print(p)
outt()'''

#print(p) P IS NOT LOCAL INSIDE THE FUNCTION ONLY
# LEGB RULE FOLLOWS
'''
w = 3
def ouut():
    w = 4
    def iin():
        w = 9
        print(w)
    iin()
    print(w)
ouut()
print(w)

w = 3
def ouut():
    w = 4
    def iin():
        print(w)
    iin()
    print(w)
ouut()
print(w)

w = 3
def ouut():
    def iin():
        print(w)
    iin()
    print(w)
ouut()
print(w)
'''




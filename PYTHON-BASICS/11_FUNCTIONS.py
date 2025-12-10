# FUNCTION
"""
1. Function definition
def(keyword to represent a function) Func_name(*args,**kwargs,args):
    statement to execute
2. Function calling
Func_name()

"""

"""
def Addnum(a,b):
    return a+b  # HERE THE FUNCTION RETURN A VALUE THAT'S NOT GET PRINTED
Addnum(10,25)

def Addnum(a,b):
    print(a+b) # THE RESULT IS PRINTED INSIDE THE FUNCTION DEFINITION 
Addnum(12,34)

def addnum(c):
    pass
print(addnum(35))

def string():
    return "vanakam da mapla b3 la irundhu"
print(string().upper())

def string(var):
    return '{} neenga yaaru bro'.format(var)
print(string('saala'))

def string(var, name = 'xxx'):
    return '{} {}'.format(var,name)
print(string('saala','aju'))"""

#*args = positional argument : number of variable argument values
#**kwargs = keyword argument : needs key and its values of variable number of arguments
'''
def info(*args):
    return args
print(info('aju 71','krishna 15','divya 9',))# returns tuple

def info(*args):
    for i in args:
        print(i)
info('aju 71','krishna 15','divya 9')'''
'''
def info(**kwargs):
    return kwargs
print(info(name='aju',name1='krishna 15',name2='divya 9',)) # returns dict


def info(**kwargs):
    for i, j in kwargs.items():
        print(i,":",j)
info(name='aju',name1='krishna 15',name2='divya 9',)'''
'''
def info(*args,**kwargs):
    print(args)
    print(kwargs)
    
inf={'name':'aju','name1':'krishna 15','name2':'divya 9'}
agr = [1,2,3,4,5]

info(inf,agr) # returns tuple
info(*agr,**inf)'''

# Function to say leap year and number of days in a month

def leapyr(year):
    return year %4 == 0 and(year%100 != 0 or year%400 == 0)
        

mndy = [0,31,28,31,30,31,30,31,31,30,31,30,31]
def day(year,month):
    if not 1<= month <= 12:
        return 'invalid daa dei'
    if month == 2 and leapyr(year):
        return 29
    return mndy[month]
print(day(2016,2))












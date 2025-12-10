# LAMBDA FUNCTION

# lambda x(arguments):expression

# b = lambda a: a+100
# print(b(10))
#def func_name():
# print((lambda a: a+100)(10))

# even = lambda x: x%2 == 0
# print(even(10))

# a = '2 bhk'

# def return_int(a):
#     return int(a.split(' ')[0])

# (c* 9/5)+32

# b = lambda a: int(a[0])
# print(type(b('2bhk')))

# c = lambda a,b: a if a>b else b
# print(c(10,2))

# w = ['python','fsd','de','da','gen ai']
# print(sorted(w,key = lambda w:len(w)))

# map(func,iterable)

# n = [1,2,3,4]
# res = frozenset(map(lambda x: x**2,n))
# print(res)

n = ['ajeeth','','kohli','','','hardik']
# print(list(map(str.upper,n)))
# print(len(''))
# n = [1,2,3,4]
print(list(filter(lambda x: x != "",n)))
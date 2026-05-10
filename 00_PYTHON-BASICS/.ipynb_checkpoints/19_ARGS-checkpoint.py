name = 'Ajeeth'
std = 'lkg'
schl = 'ABC School'
# print('my name is',name,'i study in',std,'at',schl)
# print(f'my name is {name}, i study in {std} at {schl}')

# def details(loc,age = 17):
#     print(f'{loc},{age}')
# details('Chennai',18)

# a,b,*c = (1,2,3,4,5,6,7,8,9)
# print(a)
# print(b)    
# print(c)

# def add(*args):
#     for i in args:
#         print(i)
#     print(sum(args))
# add(1,2,3,4,5,6,7,8,9)

def person(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(f'{k} : {v}')
person(name = 'Ajeeth',age = 18,loc = 'Chennai')
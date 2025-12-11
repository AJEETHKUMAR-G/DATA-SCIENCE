def chicken(func):
    def wrapper(*args,**kwargs):
        print('CHICKEN 65')
        func(*args,**kwargs)
    return wrapper

def kalakki(func):
    def wrapper(*args,**kwargs):
        print('KALAKKI VENU')
        func(*args,**kwargs)
    return wrapper

@kalakki
@chicken
def poratta(flavour):
    print(f'{flavour} PORATTA WITH SHERVA')

poratta(('Chicken koththu','mutta koththu'))

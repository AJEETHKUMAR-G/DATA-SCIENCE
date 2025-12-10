
#y = int(n)
#print(y)
'''
try:
    n = input('username:')
    y = int(n)
    
except:
    print('invalid entry')
else:
    print(y)
finally:
    print('enamachu aagum wait panunga bro')
'''

'''
try:
    f = open('AJUTT.txt')
# MOST SPECIFIC EXCEPTIONS IN THE TOP 
except FileNotFoundError as aju:
    print(aju)
# GENERAL EXCEPTIONS AT BOTTOM
except Exception as aju:
    print('Something went wrong')
# IF THERE IS NO EXCEPTION , ELSE BLOCK WILL GET EXCUTE AS CONTINUED BY TRY BLOCK
else:
    print(f.read())
    f.close()
finally:
    print('executed')
'''
'''
try:
    f = open('AJUTXT.txt')
    if f.name == 'AJUTXT.txt':
        raise Exception
except FileNotFoundError as aju:
    print(aju)
except Exception as aju:
    print('Something went wrong')
else:
    print(f.read())
    f.close()
finally:
    print('executed')'''

    


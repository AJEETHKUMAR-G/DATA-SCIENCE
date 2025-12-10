"""
f = open('AJUTXT.txt', 'r') # READ = r
print(f.name)
print(f.mode) # GIVES THE MODE USED
print(f.read()) # READ THE TEXT FILES
f.close() # NEED TO CLOSE THE FILE

with open('AJUTXT.txt', 'r') as f: # CONTEXT MANAGER METHOD 
    f_cont = f.read()              # NO NEED TO CLOSE THE FILE AT THE END 
    print(f_cont)
print('*************************')

with open('AJUTXT.txt', 'r') as f:
    f_cont = f.readlines() # RETURNS LIST OF TOTAL FILE
    print(f_cont)
print('*************************')"""

with open('AJUTXT.txt', 'r') as f:
    f_cont = f.readline() # RETURNS FIRST LINE FROM FILE
    print(f_cont)

    f_cont = f.readline() # RETURNS SECOND LINE FROM FILE
    print(f_cont)

    f_cont = f.readline() # RETURNS THIRD LINE FROM FILE
    print(f_cont, end = ' ') # REDUCE NEXT LINE SPACE
    f_cont = f.readline() 
    print(f_cont)
print('*************************')
'''
print(f.closed) # SINCE NO NEED TO CLOSE THE FILE AS ALREADY IT GOT CLOSED BY CONTEXT MANAGER
with open('AJUTXT.txt','r') as g:
    for i in g:
        print(i,end = ' ')

with open('AJUTXT.txt','r') as h:
    j = h.read(25)
    print(j,end = ' ') # PRINTS FIRST 25 CHARACTERS

    j = h.read(25)
    print(j,end = ' ') # NEXT 25 CHARS
    
    j = h.read(25)
    print(j,end = ' ')
    
    j = h.read(25)
    print(j,end = ' ') # AFTER THE END OF CHARS IT RETURNS EMPTY STRING

with open('AJUTXT.txt','r') as f:
    size = 50
    k = f.read(50)
    print(k)
with open('AJUTXT.txt','r') as f:
    size = 10
    k = f.read(size)
    while len(k) > 0:
        print(k, end = '@')
        k = f.read(size)

with open('AJUTXT.txt','r') as h:
    j = h.read(13)
    print(j,end = ' ')
    h.seek(0) # SET VALUES FROM BEGINNING
    j = h.read(13)
    print(j,end = ' ')'''

    
   







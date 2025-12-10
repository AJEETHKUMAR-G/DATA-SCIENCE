#LOOPS

# FOR LOOP : IF YOU KNOW THE LIMIT OR RANGE
# WHILE : IF YOU DON'T KNOW THE RANGE IN MOST OF THE CASES

"""a = [12,23,4,56,77,8,9]
for i in a:
    print(i)
print("************************")

for i in range(0,11): # start, stop, step
    print(i)
print("************************")

for i in range(0,11,3): # start, stop, step
    print(i)

print("************************")
a = [12,23,4,56,77,8,9]
for i in range(len(a)):
    print(a[i])
print("************************")
 
# BREAK AND CONTINUE

a = [12,23,4,56,77,8,9]
for i in a:
    if i == 8:
        print("idho ingadhaan iruke nipaatu")
        break
    print(i)
print("************************")

a = [12,23,4,56,77,8,9]
for i in a:
     print(i)
     if i == 8:
         print("idho ingadhaan iruke nipaatu")
         break
print("************************")

a = [12,23,4,56,77,8,9]
for i in a:
     if i == 8:
         print("idho ingadhaan iruke")
         continue
     print(i)
print("************************")


a = [12,23,4,56,77,8,9]
for i in a:
    print(i)
    if i == 8:
         print("idho ingadhaan iruke")
         continue
print("************************")"""

"""# SUM OF "n" NATURAL NUMBERS

a = 0
for i in range(0,100,2):
    a = a+i
print(a)"""

# SQUARE OF NUMBERS

"""for i in range(1,12):
    sq = i**2
    print("square of",i,"is",sq)"""

# SUM OF THE SQUARES OF "n" NATURAL NUMBERS

"""a = 0
for i in range(0,5):
    s = i**2
    print("square of", i,"is",s)
    a = a+s
print(a)"""

#USE for LOOP TO GENERATE A LIST OF NUMBERS FROM 9 TO 50 DIVISIBLE BY 2

"""a = []
for i in range(9,51):
    if i%2 == 0:
        a.append(i)
print(a)"""

# PASS
"""a = [1,2,3,4]
for i in a:
    pass# RETURNS NULL"""
    
    
# NUMBER PATTERN USING NESTED FOR LOOP
'''
a = 5
for i in range(1,a):
    for j in range(1,i+1):
        print(j,end="")#end= " " to print multiple values in single line
    print("\n")'''
'''
for i in range(1,5):
    print(i*"*")
    print("\n")'''

'''for i in range(1,6):
    for j in range(6-i,0,-1):
        print(j,end=" ")
    print("\n")'''

# PRINT A LIST IN REVERSE ORDER
'''
a = [1,2,3,4,5]
#b = reversed(a)
#print(b)
#for i in b:
 #   print(i)
for i in range(4,-1,-1):
    print(a[i])'''

# PROGRAM TO DISPLAY PRIME NUMBER WITHIN A RANGE

"""for i in range(3,99):
    if i>1:
        for j in range(2,i):
            if (i%j)==0:
                break
        else:
            print(i)"""




# PRINTING TWO MULTIPLIED TABLE:

"""for i in range(1,11):
    print(i ,"*", 2,"=",i*2)"""

"""for i in range(1,11):
    a = int(input("enter a value:"))
    print(i*a)"""

"""for i in range(1,11):
    a = i * int(input("enter the value:"))
    print(a)"""

# PATTERN PROGRAMS USING FOR LOOP

# SQUARE

'''n = int(input("enter a number:"))
for i in range(n):
    for j in range(n):
        print("*",end = " ")
    print("\n")'''

# INCREASING TRIANGLE 

'''n = int(input("enter a number:"))
for i in range(n):
    for j in range(i+1):
        print("*",end = " ")
    print("\n")''' 

# DECREASAING TRIANGLE
'''
n = int(input("enter a number:"))
for i in range(n):
    for j in range(n-i): # set range to(i,n)
        print("*",end = " ")
    print("\n")'''

# RIGHT TRIANGLE
'''
n = int(input("enter a number:"))
for i in range(n):
    for k in range(i,n):     # decreasing space loop
        print(" ",end = " ")
    for j in range(i+1):      # increase star loop
        print("*",end = " ")
    print("\n")'''
"""
n = int(input("enter a number:"))
for i in range(n):
    for k in range(i+1):     # increasing space
        print(" ",end = " ")
    for j in range(i,n):
        print("*",end = " ") # decreasing star
    print("\n")"""

# HILL PATTERN
"""
n = int(input("enter a number:"))
for i in range(n):
    for k in range(i,n):     # decreasing space loop
        print(" ",end = " ")
    for j in range(i+1):      # increase star loop
        print("*",end = " ")
    for l in range(i):      # to get peak we reduce the range to i
        print("*",end = " ")
    print("\n")"""

"""n = int(input("enter a number:"))
for i in range(n):
    for k in range(i+1):     # increasing space
        print(" ",end = " ")
    for j in range(i,n):
        print("*",end = " ") # decreasing star
    for j in range(i,n-1):
        print("*",end = " ")
    print("\n")
"""

# DIAMOND PATTERN
'''n = int(input("enter a number:"))
for i in range(n-1):
    for k in range(i,n):     # decreasing space loop
        print(" ",end = " ")
    for j in range(i+1):      # increase star loop
        print("*",end = " ")
    for l in range(i):      # to get peak we reduce the range to i
        print("*",end = " ")
    print("\n")
for i in range(n):
    for k in range(i+1):     # increasing space
        print(" ",end = " ")
    for j in range(i,n):
        print("*",end = " ") # decreasing star
    for j in range(i,n-1):
        print("*",end = " ")
    print("\n")'''

# NUMBER PATTERNS
""" #1
n = int(input("enter the number:"))
for i in range(n):
    for j in range(i+1):
        print("1",end=" ")
    print("\n")"""

#2
'''
n = int(input("enter the number:"))
for i in range(n):
    for j in range(i+1):
        print(i+1,end=" ")
    print("\n")
# ALITER
P = 1
n = int(input("enter the number:"))
for i in range(n):
    for j in range(i+1):
        print(P,end=" ")
    P+=1
    print("\n")'''
#3
"""
n = int(input("enter the number:"))
p = n
for i in range(n):
    for j in range(i+1):
        print(p,end=" ")
    p-=1
    print("\n")"""
#4
"""
n = int(input("enter the number:"))
p = n
for i in range(n):
    for j in range(i,n):
        print(p,end=" ")
    p-=1
    print("\n")"""

#5

'''
n = int(input("enter the number:"))
p = 0
for i in range(n):
    for j in range(i+1):
        print(p,end=" ")
    p+=2
    print("\n")
'''

#6
'''
n = int(input("enter the number:"))
for i in range(n):
    for j in range(i+1):
        if(i%2 == 0):
            print("1",end=" ")
        else:
            print("2",end= " ")
    print("\n")

'''
#7
"""
n = int(input("enter the number:"))
for i in range(n):
    p = 1
    for j in range(i+1):
        print(p,end=" ")
        p+=1
    print("\n")"""

#8
"""
n = int(input("enter the number:"))
for i in range(n):
    p = 1
    for k in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print(p,end=" ")
        p+=1
    print("\n")"""

#9
'''
n = int(input("enter the number:"))
for i in range(n):
    p = 1
    for k in range(i,n):
        print(' ',end=" ")
    for j in range(i+1):
        print(p,end=" ")
        p+=1
    for j in range(i):
        print(p,end=" ")
        p+=1
    print("\n")'''

#10
"""
n = int(input("enter the number:"))
for i in range(n):
    p = n
    for j in range(i,n):
        print(p, end = " ")
        p-=1
    print("\n")"""

#11
'''
n= int(input("enter the number:"))
k = n
for i in range(n):
    p = k
    for j in range(i+1):
        print(" ",end= " ")
    for o in range(i,n):
        print(p, end = " ")
        p-=1
    k-=1
    print("\n")'''
        
#12
'''
n = int(input("enter the number:"))
for i in range(n):
    p = 1
    for k in range(i,n):
        print(' ',end=" ")
    for j in range(i):
        print(p,end=" ")
        p+=1
    for u in range(i+1):
        print(p,end= " ")
        p-=1
    print("\n")'''
#13 FLOYD TRIANGLE
"""n = int(input("enter the number:"))
p = 1
for i in range(n):
    for j in range(i+1):
        print(p,end = " ")
        p+=1
    print("\n")"""

#ALPHABETICAL PATTERN PROGRAM

#1
"""n = 5
for i in range(n):
    for j in range(i+1):
        print(chr(65),end = " ")
    print()"""

#2
"""
n = 5
l = 65
for i in range(n):
    for j in range(i+1):
        print(chr(l),end = " ")
        l+=1
    print()"""

#3
"""
n = 5
l= 69 
for i in range(n):
    for j in range(i+1):
        print(chr(l),end = " ")
    l-=1
    print()"""

#4
"""
n = 5
l= 65 
for i in range(n):
    for j in range(i+1):
        print(chr(l),end = " ")
    l+=2
    print()"""

#5
"""n = 5 
for i in range(n):
    for j in range(i+1):
        if(i%2 == 0):
            print(chr(65),end = " ")
        else:
            print(chr(66),end= " ")
    print()"""

#6
"""
n = 5 
for i in range(n):
    for k in range(i+1):
        print(" ",end = " ")    
    for j in range(i,n):
        if(i%2 == 0):
            print(chr(90),end = " ")
        else:
            print("0",end= " ")
    print()
"""

#7
'''
n = 5
l= 65
for i in range(n-1):
    for j in range(i,n):
        print(" ",end = " ")
    for k in range(i):
        print(chr(l),end = " ")
    for h in range(i+1):
        print(chr(l),end = " ")
    l+=1
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end = " ")
    for j in range(i,n):
        print(chr(l),end = " ")
    for u in range(i,n-1):
        print(chr(l),end = " ")
    l+=1
    print()
'''
#8
'''
n = 5
l= 65
for i in range(n-1):
    for j in range(i,n):
        print(" ",end = " ")
    for k in range(i):
        print(chr(l),end = " ")
    for h in range(i+1):
        print(chr(l),end = " ")
    l+=1
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end = " ")
    for j in range(i,n):
        print(chr(l),end = " ")
    for u in range(i,n-1):
        print(chr(l),end = " ")
    l-=1
    print()'''

#9
'''
n = 5
for i in range(n):
    l = 65
    for j in range(i+1):
        print(chr(l),end = " ")
        l+=1
    print()'''

#10
''''
n = 5
for i in range(n):
    l = 65
    for k in range(i+1):
        print(" ",end = " ")
    for j in range(i,n):
        print(chr(l),end = " ")
        l+=1
    print()'''

#11
'''
n = 5
for i in range(n):
    l = 65
    for j in range(i,n):
        print(" ",end = " ")
    for i in range(i+1):
        print(chr(l),end = " ")
        l+=1
    for k in range(i):
        print(chr(l),end = " ")
        l+=1
    print()'''

#12

"""n = 5
for i in range(n):
    l = 69
    for j in range(i+1):
        print(chr(l),end = " ")
        l-=1
    print()"""

#13
'''
n = 5
l = 69
for i in range(n):
    k = l
    for j in range(i+1):
        print(" ",end = " ")
    for j in range(i,n):
        print(chr(k),end = " ")
        k-=1
    l-=1
    print()'''
#14
'''
n = 5
for i in range(n):
    l = 65
    for j in range(i,n):
        print(" ",end = " ")
    for k in range(i):
        print(chr(l),end = " ")
        l+=1
    for h in range(i+1):
        print(chr(l),end = " ")
        l-=1
    print()'''

#14
'''
a = "AJEETH"
for i in range(len(a)):
    for j in range(i+1):
        print(a[j],end = " ")
    print()
'''
#15
'''
a = "AJEETH"
p = 0
for i in range(len(a)):
    for j in range(i+1):
        print(a[p],end = " ")
    p+=1
    print()'''

#16
"""a = "AJEETH"
n = len(a)
p = n-1
for i in range(n):
    for j in range(i+1):
        print(a[p],end = " ")
    p-=1
    print()"""

#17
'''
a = "AJEETH"
n = len(a)
for i in range(n):
    p = n-1
    for j in range(i+1):
        print(a[p],end = " ")
        p-=1
    print()
'''
#18
'''
a = "AJEETH"
n = len(a)
p = n-1
for i in range(n):
    h = p
    for k in range(i+1):
        print(" ", end = " ")
    for j in range(i,n):
        print(a[h],end = " ")
        h-=1
    print()
    p-=1
    '''


# HOLLOW PATTERNS

#1
'''
n = int(input("enter a value:"))
for i in range(n):
    for j in range(n):
        if(j==0 or j == n-1):
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print()'''

#2
'''
n = int(input("enter a value:"))
for i in range(n):
    for j in range(n):
        if(i==n//2 or j == n//2):
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print()'''

#3
'''
n = int(input("enter a value:"))
for i in range(n):
    for j in range(n):
        if(j== i or j+i == n-1):
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print()'''

#4
'''
n = int(input("enter a value:"))
for i in range(n):
    for j in range(n):
        if(j==0 or j == n-1 or i == 0 or i == n-1):
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print()'''

#5
'''
n = int(input("enter a value:"))
for i in range(n):
    for j in range(i+1):
        if(i==j or i == n-1 or j == 0):
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print()'''
#6
'''
n = int(input("enter a value:"))
for i in range(n):
    for j in range(i,n):
        if(i==j or j == n-1 or i == 0):
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print()'''
#7
'''
n = int(input("enter a value"))
for i in range(n):
    for j in range(i,n):
        print(" ",end =" ")
    for j in range(i):
        if(i == n-1 or j == 0):
            print("*",end = " ")
        else:
            print(" ",end = " ")
    for j in range(i+1):
        if(i == n-1 or j == i):
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print()
'''
#8
'''
n= int(input("enter a value:"))
for i in range(n-1):
    for j in range(i,n-1):
        print(" ",end = " ")
    for j in range(i):
        if(j==0):
            print("*",end = " ")
        else:
            print(" ",end = " ")      
    for j in range(i+1):
        if(j==i):
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print()
for i in range(n):
    for j in range(i):
        print(" ",end = " ")
    for j in range(i,n):
        if(j==i):
            print("*",end = " ")
        else:
            print(" ",end = " ")
    for j in range(i,n-1):
        if(j==n-2):
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print()'''
'''
n = int(input("enter the number:"))
for i in range(1,n+1):
    count = 0
    for j in range(1,i+1):
        if(i%j==0):
            count+=1
    if count ==2:
        print(i)
'''
        

# WHILE
'''x = 0
while x < 10:
    print(x)
    x +=1
print("************************")'''
'''
x = 0
while x < 10:
    print(x)
    x +=2
print("************************")

x = 0
while x < 11:
    if x == 6:
        break
    print(x)
    x +=1
print("************************")

x = 0
while x < 11:
    print(x) 
    if x == 6:
        break
    x +=1
print("************************")'''

"""x = 0
while True:    # infinite loop
    print(x)     # ctrl + c to stop the loop
    x +=1"""
'''
hi = True
while hi:
    name = int(input("enter something"))
    if name == 0:
        print("you entered 0 so program has ended")
        break'''
'''   
while True:
    password = input("enter something: ")
    if password == "stop":
        print("stoped broo")
        break
'''
'''
i = 1
while i<73:
    if(i%4==0 or i%7==0):
        print(i)
    i+=1'''

"""i = 10
while(i<=200):
    print(i)
    i+=10"""

"""i = 10
while(i>0):
    print(i)
    i-=1"""

"""n = int(input("enter a number:"))
fac = 1
while(n>0):
    fac = fac*n
    n-=1
print(fac)"""
"""
n = int(input("enter the number"))
flag = 0
i = 2
while i<n:
    if n%i == 0:
        flag = 1
    i+=1
if flag == 1:
    print(n,"not a prime")
    
else:
    print(n," is prime")"""

# PROGRAM TO SUM OF DIGITS ACCEPTED FROM THE USER
"""
n = int(input("enter the number:"))
r = 0
s = 0
while n!=0:
    r = n%10
    s = s+r
    n = n//10
print("sum of digit is:",s)"""

# PROGRAM TO GET THE PRODUCT OF DIGITS
"""
n = int(input("enter the number:"))
r = 1
s = 1
while n!=0:
    r = n%10
    s = s*r
    n = n//10
print("sum of digit is:",s)"""

# PROGRAM TO REVERSE A NUMBER
"""
n = int(input("enter the number:"))
r = 0
renum = 0
while(n!=0):
    r = n%10
    renum = renum*10 + r
    n = n//10
print(renum)"""

# 234 => Two Three Four
"""
num = input("enter the number:")
l1 = list(num)
p = len(l1)
n = {0:"zero",1:"one",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Sev",8:"Eight",9:"Nine"}
i = 0
while i<p:
    print(n[int(l1[i])],end = ' ')
    i+=1"""

# FIBONACCI SERIES
"""
n = int(input("enter the number"))
if (n==1):
    print("1")
elif (n==2):
    print("1,1")
elif (n<=0):
    print("positive number kudu man")
else:
    a1 = 1
    a2 = 1
    i = 2
    print(a1,end = " ")
    print(a2, end = " ")
    while(i<n):
        an = a1 + a2
        print(an , end= " ")
        a1 = a2
        a2 = an
        i+=1"""

# ARMSTRONG NUMBER

n = input("enter the number:")
listed = list(n)
p = len(listed)
i = 0
r = 0
while i<p:
    r = r + int(listed[i])**p
    print(r)
    i+=1  
if r == int(n):
    print("it is armstrong number")
else:
    print("its not armstrong number")

# GET INPUT OF INTEGERS UNTIL THE USER ENDS AND TO DISPLAY SUM OF NUMBERS AT LAST
"""
ch = 'y'
s = 0
while ch == 'y' or ch == 'Y':
    num = int(input("enter the number:"))
    s = s+ num
    ch = input("continue pandrelaa dude:")
print(s)"""

# COUNTING POSITIVE AND NEGATIVE INTEGERS
"""
ch = 0
pcount = 0
ncount = 0
while ch != 0:
    num = int(input("enter the number:"))
    if num > 0:
        pcount += 1
    else:
        ncount +=1
    ch = input("enter pandrela 0/1:")
print("positive counts",pcount)
print("negative counts", ncount)"""

# HCF OF TWO NUMBERS
'''
num1 = int(input("enter the number:"))
num2 = int(input("enter the number:"))
rem = 1
if num1 > num2:
    while rem!=0:
        rem = num1%num2
        if rem == 0:
            hcf = num2
        else:
            num1 = num2
            num2 = rem
else:
    while rem!=0:
        rem = num2%num1
        if rem == 0:
            hcf = num1
        else:
            num2 = num1
            num1 = rem
print(hcf)'''

# DECIMAL TO BINARY
'''
dec = int(input("enter the value"))
bina = 0
p = 1
n = dec
while n>0:
    rem = int(n%2) # if int is not said..it will raise overflow error
    bina = bina + rem*p
    p = p*10
    n = n/2
print(bina)'''

# BINARY TO DECIMAL
'''
bina = int(input("enter the binary value"))
dec = 0
i = 0
while bina>0:
    rem = bina%10
    dec = dec + rem *(2**i)
    i+=1
    bina = bina // 10
print(dec)'''
   
            



























    
    










































        
   

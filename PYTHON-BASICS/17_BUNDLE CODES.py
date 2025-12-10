def IncreasingNumPat(x):
    for i in range(x):
        for j in range(i+1):
            print(j+1,end = ' ')
        print()
def DecreasingNumPat(x):
    for i in range(1,x):
        for j in range(i,x):
            print(j,end = ' ')
        print()
def Sum_of_Squares(n):
    s = 0
    for i in range(1,n+1):
        s+=i
    print(s)
def Range_of_Primes(a,b):
    for i in range(a,b+1):
        if i>0:
            for j in range(2,i):
                if i%j == 0:
                    break
            else:
                print(i)
def UpHill_Pattern(x):
    for i in range(x):
        for j in range(i,x):
            print(' ',end = ' ')
        for k in range(i+1):
            print('*', end = ' ')
        for o in range(i):
            print('*',end = ' ')
        print()
def DownHill_Pattern(x):
    for i in range(x):
        for j in range(i+1):
            print(' ' ,end = ' ')
        for k in range(i,x):
            print('*',end = ' ')
        for o in range(i,x-1):
            print('*',end = ' ')
        print()
def Diamond_StarPattern(x):
    for i in range(x-1):
        for j in range(i,x):
            print(' ',end = ' ')
        for k in range(i+1):
            print('*', end = ' ')
        for o in range(i):
            print('*',end = ' ')
        print()
    for i in range(x):
        for j in range(i+1):
            print(' ' ,end = ' ')
        for k in range(i,x):
            print('*',end = ' ')
        for o in range(i,x-1):
            print('*',end = ' ')
        print()
def Floyd_Triangle(x):
    p=1
    for i in range(x):
        for j in range(i+1):
            print(p,end = ' ')
            p+=1
        print()
def Parallel_Line(x):
    for i in range(x):
        for j in range(x):
            if j==0 or j== x-1:
                print('*',end = ' ')
            else:
                print(' ',end = ' ')
        print()
def Hollow_Diamond(n):
    for i in range(n-1):
        for j in range(i,n-1):
            print(' ', end= ' ')
        for j in range(i):
            if j == 0:
                print('*', end = ' ')
            else:
                print(' ',end = ' ' )
        for j in range(i+1):
            if j == i:
                print('*', end = ' ')
            else:
                print(' ',end = ' ' )
        print()
    for i in range(n):
        for j in range(i):
            print(' ', end = ' ')
        for j in range(i,n):
            if i == j:
                print('*', end = ' ')
            else:
                print(' ', end = ' ')
        for j in range(i,n-1):
            if j == n-2:
                print('*', end = ' ')
            else:
                print(' ',end = ' ')
        print()
def Factorial(n):
    s = 1
    while n > 0:
        s = s*n
        n-=1
    print(s)
def Check_Prime(n):
    i = 2
    flag = 0
    while i<n:
        if n%i == 0:
            flag = 1
        i+=1
    if flag == 1:
        print('NOT PRIME')
    else:
        print('PRIME')
def Sum_of_Digits(n):
    s = 0
    r = 0
    while n!= 0:
        r = n%10
        s = s+r
        n = n//10
    print('SUM OF DIGITS IS:',s)
def Reverse_digits(n):
    s = 0
    r = 0
    while n !=0:
        r = n%10
        s = s*10 + r
        n = n//10
    print('REVERSED DIGIT IS,',s)
def Name_the_Digits(n):
    a = []
    while n != 0:
        r = n%10
        a.append(r)
        n= n//10
    
    b = list(reversed(a))
    i = 0
    p = len(b)
    n = {0:'ZERO',1:'ONE',2:'TWO',3:'THREE',4:'FOUR',5:'FIVE',6:'SIX',7:'SEVEN',8: 'EIGHT',9:'NINE'}
    while i<p:
        print(n[int(b[i])],end= ' ')
        i+=1
def Fibonacci_Series(n):
    if n == 1:
        print(1,end = ' ')
    elif n == 2:
         print(1,end = ' ')
    elif n<= 0 :
        print('FIBONACCI DOES NOT EXIST')
    else:
        a1 = 1
        a2 = 1
        print(a1,end = ' ')
        print(a2, end = ' ' )
        i = 2
        while i < n:
            an = a1 + a2
            print(an , end = ' ')
            a1 = a2
            a2 = an
            i+=1
def Armstrong(n):
    l = str(n)
    u = list(l)
    p = len(u)
    s = 0
    i = 0
    while i < p:
        s = s+ int(u[i])**p
        i+=1
    if s == int(l):
        print('IT IS ARMSTRONG')
    else:
        print('NOPE')
def HCF(num1, num2):
    rem = 1
    if num1>num2:
        while rem != 0:
            rem = num1%num2
            if rem == 0:
                hcf = num2
            else:
                num1 = num2
                num2 = rem
    else:
        while rem != 0:
            rem = num2%num1
            if rem == 0:
                hcf = num1
            else:
                num2 = num1
                num1 = rem
    print(hcf)
def Dec_to_Bin(x):
    binary = 0
    p = 1
    n = x
    while n > 0:
        rem = int(n%2)
        binary = binary + rem * p
        p = p * 10
        n = n/2
    print(binary)
def Bin_to_Dec(x):
    decimal = 0
    i = 0
    while x> 0:
        rem = x%10
        decimal = decimal + rem*(2**i)
        i+=1
        x = x//10
    print(decimal)
def Leap_year(x):
    if x%4 == 0 and ( x%100 != 0 or x%400 == 0):
        print('Leap year')
def Year_Month(x,y):
    m = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    if not 1<= y <= 12:
         print('INVALID ENTRY')
    elif y == 2 and Leap_year(x):
          print('29')
    else:
        print(m[y])


        
    
        
        


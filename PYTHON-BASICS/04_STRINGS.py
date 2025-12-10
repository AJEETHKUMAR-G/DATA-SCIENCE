#4. STRINGS
'''
"""msg =  "Hello bro!., what's your name"
name = input("enter the name: ")
print(msg , "\n hi my name is", name)"""

#message = 'aju's py world' THIS LINE DOES'NT KNOW WHERE THE STRING GETS END

message = 'aju\'s py world'
print(message) # or
msg = "aju's py world"
print(msg) 
#a = """cristiano ronaldo won saudis special
#salman cup tournament and made a record"""
print(a)

'''
# b = "Innum Konja Neram Irundha Dha Ennaaa"
# print("the length of the string is:", len(b))
# print("lowercase:", b.lower())
# print("uppercase:", b.upper())
# print("Counting the letter or word:", b.count("n") + b.count("N"))
# print(b.find("Dha"))
# print(b.find("yen"))
# c = b.replace("Konja","romba")
# print(c)
# print(b)

# d = "yen avasaram enna avasaram nillu ponne"
# print(b + d)
# print(b+ " " +d)

# new = b + " " + d +" nee yen kannu pola irukanum "
# print(new)

# print("**********************************")
# formt = "{} {} nee yen kannu pola irukanu".format(b.replace('Neram','time'),d)
# print(formt)
# f_string = f"{b} {d.upper()} innu pesa kooda thodangala"
# print(f_string)
# print('directary',dir(d))
# print("************************")
# print(help(str))

# j = "   naan unai neenga maaten "
# print(j)
# print(j.strip()) # Removes unwanted spaces
# print(j.split('a')) # Split by the delimeter given as argument
# print("**********************************************************************")

#SLICING
   # 0123456789
# s = "kannana kanne nee kalangadha"
#    #                            -1   
# print("Slicing:",s[3])
# print(len(s))# lenght of s is "28" [0 to 27]
# print(s[27])
# #print(s[28])  raise index error
# print(s[-1])
# print(s[7])
# print(s[-14])
# print(s[0:2]) #s[start:stop:step]
# print(s[5:28])
# print(s[-1:])
# print("Negative slicing:",s[-1:-17])# It shows nothing in the output
# print("Negative slicing:",s[-1:-17:-1])
# print(s[-20:-4])
# print(s[-1::])
# print(s[-1::-1])
# print(s[::3])
# print(s[-1:-9:2])# shows nothing
# print(s[-1:-9:-2])
# print(s[:-1:])
# print(s[:-1:-2]) # shows nothing


# Create a string made of the first, middle and last character

# a = 'james'
# b = a[0]+a[int(len(a)/2)]+a[len(a)-1]
# print(b)


# string made of middle 3 letters

# a = 'jhondipeta'
# b = a[int(len(a)/2)-1]+a[int(len(a)/2)]+a[int(len(a)/2)+1]
# print(b)

#Append new string in the middle of a given string

# a1 = 'Ault'
# a2 = 'Kelly'
# n = int(len(a1)/2)
# b = a1[:n]+ a2+ a1[n:]
# print(b)


# a = "ajuajukrishna"
# c = 0
# for i in a:
#     if i == 'a':
#         c+=1
# print(c)

# def string_fml(a):
#     name = a
#     n = int(len(a))
#     print(name[0]+name[int(n/2)]+name[n-1])
# string_fml('japan')














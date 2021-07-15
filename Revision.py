# Print

print("Hello world!")

name = "Nisarg"

print("Hello", name)

print("Hello {}".format(name))

# Data types

a = 10
b = -100
c = 9.81
d = "Python"
e = 5+5j
f = True

print(type(a), type(b), type(c), type(d), type(e), type(f))

# Input

x = input("Enter any number ") 
print(x)
print(type(x)) # By Default String

x = int(input("Enter any number "))  # Type Casting
print(x)
print(type(x))

# Arithmetic Operators

a = 51
b = 23

print(a+b)
print(a-b)
print(a*b)
print(a/b) # True Division
print(a//b) # Floor Division
print(a%b)  # Modulo --> remainder
print(a**b)  # Power Of

# Relational Operator  --> Always return a bool value

print(a>b)
print(a<b)
print(a<=b)
print(a>=b)
print(a==b)
print(a!=b)

# Assigment Operator

a = 12 # Assign
a += 2 #Add and Assign
a -= 2 #Subtract and Assign
a /= 2
a //= 2
a *= 2
a **=2
a %=2

a,b,c,d = 1,2,3,4  # Multiple Assignment

# Logical Operators
# and, or, not


True and True
a>b and d<c

False or True
a>b or d<c

not True
not a>b

# Membership Operator  -- > Returns Boolean
# in & not in

"Py" in "Python"

# for(int i = 0; i < 5; i++)
for i in range(5):
    pass

print(1 not in [4,2,5,6,7,1,5])

# Python Indentity -- > Returns Boolean

print(2 is 2.00)  # Resemble ==
print(2 is not 2.00) # Resemble !=


# Bitwise Operators
#Q 3 & 4 (3 and 4)
#3 ==>  011
#4 ==>  100
#=      000   ==> 0

print(3&4)  # Bitwise AND

#Q 3 | 4 (3 or 4)
#3 ==>  011
#4 ==>  100
#=      111   ==> 7

print(3|4) # Bitwise OR


#Q 7 ^ 4 (7 XOR 4)
#7 ==>  111
#4 ==>  100
#=      011   ==> 3      
print(7^4) # Bitwise XOR

print(~3)  # Bitwise 1's complement   -(x+1)

print(4<<2) # Bitwise Left shift  # 100 --> 10000

print(4>>2) # Bitwise Right shift # 100 --> 001


# Collections 

# List 

li = [1,23,45,"Python", 45.21]

#append
#pop
#remove
#insert
#expand
#Sort
#Reverse
#del
#count
#index

# Set 

s = {"Mango", "Banana", "Mango"}

#union
#intersection
#symmetry
#difference
#etc ...

# Tuple

t = ("Python", "Language")
t = ("Python") # Python
t = ("Python",) # Tuple

#index
#len

# Dictionary

d = {"Name":"Rachit", "Branch":"ME"}

#values
#keys
#items
#update
#has_key
#etc..
if not d.has_key("university"):
    d.update({"university":"University"})

# Conditional Statements 

# if, elif (else if), else
# Indentation
a = 12

if a<10:
    print("Hy")
elif a == 12:
    print("Equal")
else:
    print("Hola")


# Loops

# for and while

for i in range(5):
    pass

for i in range(10,20):
    pass

for i in range(0,10,2):
    pass

for i in li:
    pass

for i in t:
    pass

for i in "Python":
    pass

while True:
    pass

while a>45:
    pass


# Control Flow Statement

# Pass, Continue, Break,

# for else


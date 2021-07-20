# Functions are "Self Contained" modules of code that accomplish a specific task

# There are two types of functions
#   1. Predefiend Fumctions
#   2. User Defined Functions


# we use keyword "def" to define a function

# In C / Cpp
# --> declaration, Defination and calling
'''
# Declaration
void Addition(int, int);

# Defination
int Addition(int a, int b)
{
    ..
    ..
    ..



    ..
    return x
}

# Calling
int a = Addition(3,4);

'''

def Addition():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    return(a+b)



## Advantages of Functions

# 1. Reuseability
# 2. Readability
# 3. Less Lines of code
# 4. Saves Time
# 5. Saves Storage
# 6. No Repition of code
# 7. No Complex Structure


print("hello To all")
print("Python is Fun")
#sum = Addition()
print(sum)
for i in range(12):
    print(i)

print("Bye")


# Types of Functions

# 1. No Input No Output

def Add1():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a+b)

# 2. No Input Yes Output

def Add2():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    return a+b


# 3. Yes Input No Output

def Add3(x, y):
    print(x+y)


# 4. Yes Input Yes Output

def Add4(x, y):
    return(x+y)


#Add1()

#a = Add2()
#print(a)

#Add3(54,47)

#a = Add4(54)
#print(a)

print("-----------------------------")

## Default Argument

# All Default Arguments are always declared at last after all static arguments
def Add5(x,y,z=0, v = 0):
    print(x+y+z+v)

Add5(10,54,45,45)

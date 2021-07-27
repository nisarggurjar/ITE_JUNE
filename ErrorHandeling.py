# try
# except
# finally
# else
# raise

'''
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a/b)
except:
    print("You Got an Error")
finally:
    print("Block is over!")
'''

'''  
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    ans = (a/b)
    if ans>5:
        new = ans/3
    print(ans)
    
    if ans<=5:
        5+"5"

    print(new)
except ZeroDivisionError:
    print("You are trying to divide a number by zero")

except NameError:
    new = 10
    print(new)

except Exception as e: 
    print("You Got an Error, that is", e)
else:
    print("You Did Very Well!!")
'''

x = int(input("Enter any number"))

if x<0:
    raise Exception("You are not allowed to enter any number below zero")



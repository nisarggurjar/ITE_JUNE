# if
# if else
# elif

'''
rain = False

# if --> single condition
if rain == True:
    print("I will take a leave")

# if else

if rain == True:
    print("I will take a leave")
else:
    print("I will go to office")

# if else 

sunny = False

if rain:
    print("I will take a leave")
elif sunny:
    print("I will go to office")
else:
    print("I will go for a movie show")

'''
# nested if

# WAP in python to satisfy given conditions
# take input from user for gender and age
# condition 1 : age >= 16 if gender is female
# condition 2 : age >= 18 if gender is male 

#age = int(input("Enter your age: "))
#gender = input("Enter your gender: ")  # f for females and m for males

'''
if age >= 16:
    if gender == 'f':
        print("Eligible for vote")
    elif gender == 'm':
        print("Not eligible for vote")
    else:
        print("Enter a valid gender")
elif age >= 18 and (gender == 'm' or gender == 'f'):
    print("Eligible for vote")
else:
    print("Not eligible for vote")
'''

'''
if age>=16 and gender == 'f':
    print("Eligible for vote")
elif age>=18 and (gender == 'm' or gender == 'f'):
    print("Eligible for vote")
else:
    print("Not eligible for vote")
'''

'''

if age>=16 and gender is 'f':
    print("Eligible for vote")
elif age>=18 and (gender is 'm' or gender is 'f'):
    print("Eligible for vote")
else:
    print("Not eligible for vote")'''

# != -----> is not

'''
if age >= 16:
    if gender == 'f':
        print("Eligible for vote")
    elif gender == 'm':
        print("Not eligible for vote")
    else:
        print("Enter a valid gender")
elif age >= 18 and (gender is 'm' or gender is 'f'):
    print("Eligible for vote")
elif (gender is not 'f') or (gender is not 'm'):
    print("Enter a valid gender")
else:
    print("Not eligible for vote")

# Ambiguity ---> delima (confusion)  ---> Absurd 
# in C or Cpp --> print initialized variable ----> garbage  ---> Absurd
'''
#
#num = 10
#
#if num is not 10:
#    print("hello")
#else:
#    print("Bye")


# Comparision Operators
# conditional Statements
# nested conditional statements
# logical operators
# use of is and not


# Short Hand Conditional Statement

num = -8

print("Positive") if num>0 else print("Negative")   # ? : 
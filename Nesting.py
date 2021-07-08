percent = [44,65,98,77,35,46,74,99]
print(len(percent))

marks = [
    [45,67,45,98,33], 
    [78,45,51,31,85], 
    [98,89,22,85,33]
]

print(len(marks))

# Accesing Nested Element

print(marks[1])

# Accesing an element in nested element (list)

print(marks[1][2])

Distributedmarks = [
    [
        (45,12),
        (54,10),
        (70,15)
    ],
    [
        (70,19),
        (45,12),
        (30,7)
    ]
]

detailedMarks = [
    {"Name":"Rachit", "marks":[
        (45,12),
        (54,10),
        (70,15)
    ]},
    {"Name":"Humera", "marks":[
        (70,19),
        (45,12),
        (30,7)
    ]},
    {"Name":"Rhythm", "marks":[
        (87,10),
        (45,10),
        (60,15)
    ]},

]
print(detailedMarks)
print(detailedMarks[1])
print(detailedMarks[1]["marks"])
print(detailedMarks[1]["marks"][1])
print(detailedMarks[1]["marks"][1][1])



for i in range(4):
    for j in range(4):
        print(i,j, end=" ")

print("Hello")
print("to")
print("all")

print("----------------------")

print("Hello", end="")
print("to", end="")
print("all")   # default end="\n"


"""
Q. WAP to create stat pattern as shown

*
**
***
****
*****
"""

print("+"*5)

inp = int(input("Enter any Number"))

for i in range(1,inp+1):
    if i%2==0:
        print("*"*i)
    else:
        print(i*"/")

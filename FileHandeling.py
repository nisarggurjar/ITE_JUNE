'''
f = open("demo.txt", "r")

#s = f.read()
l = f.readline()
print(l)
lines = f.readlines()
#print(s)

f.close()
'''

#with open("demo1.txt", "w") as file:
#    #file.write("I am learning python")
#    file.write("It is a very intersecting language")
#    file.close()

#with open("demo1.txt", "a") as file:
#    #file.write("I am learning python")
#    file.write("It is a very intersecting language")
#    file.close()


import os

#os.rename("demo1.txt", "DemoOne.txt")

os.remove("DemoOne.txt")

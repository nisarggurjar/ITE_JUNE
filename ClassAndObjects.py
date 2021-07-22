class Human:
    species = "Homosapiens"

    def walk(self):
        print("Walking........")

    def eat(self, food):
        print("Eating........")
        print("I am a",food)
        self.food = food

    def age(self, YOB):
        self.Age = 2021-YOB
        print("Your age is: ", self.Age)

a = Human()
b = Human()
c = Human()

a.age(1996)
b.age(2000)
c.age(1999)

print(a.Age)




a.height = 6
a.weight = 80
a.name = "Apple"

print(a.height)
print(a.weight)
print(a.name)

print("---------------------------")


b.height = 5.5
b.weight = 75
b.gender = "Male"

print(b.height)
print(b.weight)
print(b.gender)

print("---------------------------")


c.lambaii = 5.5
c.wazan = 75
c.umar = 21

print(c.lambaii)
print(c.wazan)
print(c.umar)



a.eat("Veg")
a.walk()

b.eat("Non Veg")
b.walk()

c.eat("Vegan")
c.walk()

print(a.food)


## Class 
# A class is a collection of objects. Unlike the primitive data structures, classes are data structures that the user defines. They make the code more manageable.
# Class is actually a blueprint for objects which don't have existance on it's own.


## Object
# When we define a class only the description or a blueprint of the object is created. There is no memory allocation until we create its object. The objector instance contains real data or information.

# Object is actually a real time entity,

class Test1():
    pass

ob = Test1()

print(ob)

## Self:
# it holds the reference to the calling object.
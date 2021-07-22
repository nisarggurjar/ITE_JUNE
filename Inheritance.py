# Inheritance is the procedure in which one class inherits the attributes and methods of another class. The class whose properties and methods are inherited is known as the Parent class. And the class that inherits the properties from the parent class is the Child class.

# Single Inheritance (One Parent and one child)
class Bikes:

    def move(self):
        print("Mobility")

    def wheels(self):
        self.wheels = 2
        print("bikes have", self.wheels, "wheels")

class iSmart(Bikes):

    def i3S(self):
        print("It saves fuel")

    def enginePower(self):
        self.power = "110cc"
        print("Power = " + self.power)

ob = Bikes()
ob.move()
ob.wheels()

ob1 = iSmart()
ob1.i3S()
ob1.enginePower()
ob1.wheels()
ob1.move()


# Hierarchical inheritance (One Parent and multiple child)
class Bikes:

    def move(self):
        print("Mobility")

    def wheels(self):
        self.wheels = 2
        print("bikes have", self.wheels, "wheels")

class iSmart(Bikes):

    def i3S(self):
        print("It saves fuel")

    def enginePower(self):
        self.power = "110cc"
        print("Power = " + self.power)

class Fazer(Bikes):

    def BlueCore(self):
        print("It saves fuel without compromising the power")

    def enginePower(self):
        self.power = "200cc"
        print("Power = " + self.power)

# Multilevel Inheritance

class Vehicle:

    def Fuel(self):
        print("They run on fossil fuels")

class Bikes(Vehicle):

    def move(self):
        print("Mobility")

    def wheels(self):
        self.wheels = 2
        print("bikes have", self.wheels, "wheels")

class iSmart(Bikes):

    def i3S(self):
        print("It saves fuel")

    def enginePower(self):
        self.power = "110cc"
        print("Power = " + self.power)

ob = iSmart()
ob.Fuel()

# Multiple Inheritance

class Mom:
    pass

class Dad:
    pass

class Child(Mom, Dad):
    pass


# Hybrid Inheritance

class Test1:
    pass

class Test2(Test1):
    pass

class Test3(Test1):
    pass

class Test4(Test3):
    pass
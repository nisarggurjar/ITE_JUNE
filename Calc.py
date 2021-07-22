from math import *
from abc import ABC, abstractmethod
class BasicCalculator(ABC):

    def __init__(self, name):
        self.__name = name
        print("Welcome", name)

    def UpdateUsername(self, newname):
        self.__name = newname
        print(self.__name)
        
    def Addition(self,a,b):
        print(a+b)

    def Subtract(self,a,b):
        print(a-b)

    @abstractmethod
    def Division(self,a,b):
        print(a//b)

    def Multiply(self,a,b):
        print(a*b)

class AdvancedCalculator(BasicCalculator):

    def Sine(self,a):
        print(sin(a))

    def Cosine(self,a):
        print(cos(a))

    def Tangent(self,a):
        print(tan(a))

    def Division(self,a, b):
        print(a/b)



ob1 = AdvancedCalculator("Nisarg")
ob1.Addition(5,4)
ob1.Tangent(24)
ob1.Division(5,2)
ob1.UpdateUsername("Nisarg Gurjar")

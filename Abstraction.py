from abc import ABC, abstractmethod   

class A(ABC):

    def Test1(self):
        print("Test 1")

    def Test2(self):
        print("Test 2")

    @abstractmethod
    def Test3(self):
        pass

class B(A):

    def Test4(self):
        print("Test 4")

    def Test3(self):
        print("Test 3")

class C(A):
    
    def Test3(self):
        print("Test 3 from class C")

ob = C()
ob.Test3()
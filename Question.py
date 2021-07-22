class Test1:

    def __init__(self):
        print("Hello")
    
    def Any(self):
        print("This is a function of class Test1")

class Test2(Test1):
    
    def __init__(self):
        print("Hy")
        super().__init__()
        super().Any()

    def KuchBhi(self):
        print("This is a function of class Test2")

ob = Test2()


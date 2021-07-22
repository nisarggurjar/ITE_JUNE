class Rachit:

    def Intro(self):
        print("This is the Introduction of Rachit")

    def DOB(self):
        print("21 Dec 1991")


class Humera:

    def Intro(self):
        print("This is the Introduction of Humera")

    def DOB(self):
        print("24 Oct 1991")

ob = Humera()
ob.Intro()

ob2 = Rachit()
ob2.Intro()


class Calculator:

    def add(self, a, b):
        print("This is first function")
        print(a+b)

    def add(self, a, b):
        print("This is second function")
        print(a+b)

    def add(self, a, b):
        print("This is third function")
        print(a+b)


ob = Calculator()
ob.add(4,5)

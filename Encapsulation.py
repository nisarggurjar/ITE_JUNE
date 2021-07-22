class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.__rollno = rollno   # Name Mangling (_<ClassName>__attribute)
        print("Hello, {} your roll number is {}".format(name, rollno))

    def GetInfo(self):
        print("Hello, {} your roll number is {}".format(self.name, self.__rollno))

    def SetRoll(self, roll):
        self.__rollno = roll

ob = Student("rachit", 1)
ob.name = "Rachit"
ob.GetInfo()
ob.SetRoll(10)
ob.GetInfo()
#print(dir(ob))

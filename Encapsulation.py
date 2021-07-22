class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        print("Hello, {} your roll number is {}".format(name, rollno))

    def GetInfo(self):
        print("Hello, {} your roll number is {}".format(self.name, self.rollno))


ob = Student("rachit", 1)
ob.name = "Rachit"
ob.GetInfo()
ob.rollno = 25
print(ob.rollno)
ob.GetInfo()

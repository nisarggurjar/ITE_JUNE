class Car:

    def __init__(self, model, make):
        self.model = model
        self.__make = make
        self.__Age = 2021-self.__make

        print("Model is {} and age is {}".format(self.model, self.__Age))

    def getInfo(self):
        print("Model is {} and age is {}".format(self.model, self.__Age))

    def updateInfo(self, model, make):
        self.model = model
        self.__make = make
        self.__Age = 2021-self.__make

    def UpdateMake(self, make):
        self.__make = make
        self.__Age = 2021-self.__make


ob = Car("Maruti", 2015)
ob.model = "TATA"
ob.getInfo()
ob.UpdateMake(2016)
ob.getInfo()

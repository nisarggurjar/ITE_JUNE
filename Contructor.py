class Student:
    
    institue = "Puffin India Pvt. Ltd."

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        print("Hello To ", name)        

a = Student("John", 1)

print(a.name)
print(a.roll)
print(a.institue)

b = Student("Doe", 2)


print(b.name)
print(b.roll)
print(b.institue)

c = Student("Vicky", 3)

print(c.name)
print(c.roll)
print(c.institue)


print(institue)
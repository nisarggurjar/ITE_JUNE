## Dictionary ---> Stores values(elements) in the form of (key, value) pairs

dic = {"name":"Nisarg", "email":"nisarggurjar16@gmail.com", "phone":9179562354}

print(dic)

# it dont have any indexing
# it is advised to use unique keys for diffrent elements in dictionary

dic = {"name":"Nisarg", "email":"nisarggurjar16@gmail.com", "phone":9179562354}


print(dic["name"])
print(dic["email"])

# Functions of Dictionary


print(dic.values())
print(dic.keys())

dic["lastName"] = "Gurjar"
print(dic)

dic.update({"branch":"CSE"})
print(dic)

dic.update({"email":"nisarggurjar@ymail.com"})
print(dic)

print(len(dic))

#print(str(dic))

print(dic.items())

dic.clear()
print(dic)

del dic

print(dic)

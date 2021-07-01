# List ---> Hetrogeneous Types, Dynamic allocation, mutable

li = [1, 2, 3, 4, 5, 6, 3.14, 9.8, 8.3, "Humera", "Rachit", 4+5j]
print(li)
print(type(li))

# Empty List

li1 = []
print(li1)
print(type(li1))

li2 = list()
print(li2)
print(type(li2))

li3 = [1]
print(li3)
print(type(li3))

## Functions of list

# Append ---> Add an element at the end of the list
li.append(400)
print(li)

#pop ---> Remove an element from end / particular index of the list
a = li.pop()  # By default remove from the end
print(a)
print(li)

b = li.pop(-4)
print(b)
print(li)

#Insert ---> Add an element at a particular index
li.insert(3, 3.5)   # <list_name>(position, element)
print(li)

li = [1,2,5,4,7,1,4,5,6,2,9,8,7,2,6,2,3,4,1,23,4,5,8]

# index ---> it returns the index of a particular element
i = li.index(7)
print(i)
print(li[i])

# Count
c = li.count("Rachit")
print(c)

# Remove
print(li)
li.remove(7)
print(li)
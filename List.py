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

li = [1,2,5,4,7,1,4,5,6,2,9,8,7,2,6,2,3,4,1,4,5,8]

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

#Extend ---> To add multiple elements
li.extend((10,12,14,16,18))
print("Extended Li",li)

# Sort

li.sort()
print(li)

# Reverse
li.reverse()
#li.sort(reverse=True)
print(li)


# Copying list

li1 = [1,2,3]
li2 = []

li2 = li1
print(li1)
print(li2)

li1.append("Python")

print(li1)
print(li2)


##
##  Name of an array always represents its base address
##  int a[] = {1,2,3,4,5}
##  &a
##  a

li1 = [1,2,3]
li2 = []

li2 = li1.copy()

li1.append("Python")

print(li1)
print(li2)

# Clear

print(li)
li.clear()

######## Not The Functions of List but are commonly used with list

li = [1,2,5,4,7,1,4,5,6,2,9,8,7,2,6,2,3,4,1,4,5,8]

## Length
a = len(li)
print(a)
#
## Maximum
b = max(li)
print(b)
#
## Minimum
c = min(li)
print(c)
#
## Total / Sum
s = sum(li)
print(s)

# Delete
del li
print(li)
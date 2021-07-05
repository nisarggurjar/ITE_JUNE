## Set 

s = {"london", "NYC", "Canada", "India", "Korea", "london"}
# Unorederd, # Unchangeable, Duplicates are not allowed

print(s)

print(len(s))

s = {"london", 35, 45.566, "India", 4+5j, "london"}
print(s)

s1 = {1,2,3,4,5,6,7,8,9,10}
s2 = {2,4,6,8,10}
s3 = {1,3,5,7,9}


print(s2.issubset(s1))

print(s1.issuperset(s2))

print(s1.difference(s2))

print(s2.union(s3))

print(s2.intersection(s1))



'''
x=0
y=1

print(x)
print(y)

for i in range(0,10):
    c=x+y
    x,y=y,c #using swap
    # x=y
    # y=c
    print(c)
'''


x = 0
y = 1

c = 1
while c:
    c=x+y
    if c>=100:
        break
    x,y=y,c #using swap
    # x=y
    # y=c
    print(c)
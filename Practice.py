def Addition(a, b):
    return a+b

def Subtract(a, b):
    return a-b

def Multiply(a, b):
    return a*b

def TrueDivision(a, b):
    return a/b

def FloorDivision(a, b):
    return a/b

def Remainder(a, b):
    return a%b

def Power(a, b):
    res = 1
    while b>0:
        res = res*a
        b-=1
    return res

def Power1(a, b):
    s = str(a)
    for i in range(b-1):
        s = s + '*' + str(a)
    return eval(s)

print(Power1(2,4))



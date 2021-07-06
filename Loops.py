# C/C++ ---> For, While, do While

# JS ===> For, While, do While, for each loop


# Python ---> For, While

##  Range

range(0,10)  #==> 0,1,2,3,4,5,6,7,8,9
range(10,16) #==> 10,11,12,13,14,15
range(5)  # ==> 0,1,2,3,4
range(0,10,2)  #==> 0,2,4,6,8


# C
'''
for(int i=1; i<11; i++)
{
    cout<<i*2;
    i++  => i=i+1 => i+=1
}
'''

'''
for i in range(0,11):
    print(i)


num = int(input("Enter any number "))

for i in range(1,11):
    print(num," X ", i, " = ", num*i)


# (1,5) -> 2,3,4
# [1,5] -> 1,2,3,4,5j
# [1,5) -> 1,2,3,4


for i in range(0,20, 2):
    print(i)

'''

'''
arr[5] = {1,2,3,4,5};
for(int i = 0, i<len(arr), i++)
{
    printf("%d", arr[i]);
}


js

arr[5] = {1,2,3,4,5};

for each i in arr:
{
    print(i)
}
'''

li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

for i in li:
    print(i)

li1 = ["Rachit", "Humera", "Gourav", "Rhythm"]

for i in li1:
    print(i)

print("-------------------------")

for i in range(len(li1)):
    print(li1[i])

"""
Q. WAP to find wether a given number is prime or not.
"""

num = int(input("Enter any Number"))

#1. num%1 == 0  
#2. num%num == 0
#3. num%x != 0 (x is set of all natural number except 1 and num)
#4. for checking prime number,  x < num

for x in range(2,num):  # condition 1,2,4 is checked
    if num%x == 0:
        print("Not a prime number")
        break
    else:
        print("Prime Number")

'''
#### pass, continue and break

## Pass----> 

for x in range(2,num):  # condition 1,2,4 is checked
    if num%x == 0:
        pass
    else:
        pass


## Continue 

for x in range(15):
    if x%5==0:
        print(x,"Hy")
        continue
    else:
        print(x,"Hello")
        print(x)
    print(x,"This is Python")

print("_----------------------------------------------------------------")
## Break
for x in range(1,15):
    
    if x%5==0:
        print(x,"Hy")
        break
    else:
        print(x,"Hello")
        print(x)
    print(x,"This is Python")

'''
#We usually write Continue and break inside a conditional statement

'''
'''
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
    print("prime number")

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


'''
Q. from a given list of random element (elements can be a string, int, float) we have to seprate them in diffrent lists?

let li = [1,5,4, "Humera", 4.5 8.7 , 4,  5, "Rachit"]

liStr = ["Humera", "Rachit"]
liInt = [1,5,4,4,5]
liFloat = [4.5, 8.7]
'''


## for else  ---> the else block, will operate only if loop is terminated normally 

# normal termination of loop means loop is fully executed and there is no break applied in between
# abnormal termination --> whenever loop ends due to any abnormal conditions such as break statement

li = {1,5,4, "Humera", 4.5, 8.7 , 4,  5, "Rachit"}
for i in li:
    print(i)


s = "I am a python developer"
for i in s:
    print(i)

#Q. iterate through dictionary



############################
######### While ############
############################
i = 1
while i<15:
    print(i)
    i+=1
print("---------------------------")
li = [1,5,4, "Humera", 4.5, 8.7 , 4,  5, "Rachit"]

#while True:
#    print("Hy")
i = 0
while i<len(li):
    print(li[i])
    i+=1    # i = i + 1

ch = 'y'

while ch == 'y':
    print("program is running")
    ch = input("Do you want to continue? (press y for yes)")


# WAP a program for a basic calculator

ch = 'y'

while ch == 'y' or ch == 'Y':
    num1 = int(input("Enter First Number"))
    num2 = int(input("Enter Second Number"))

    op = input("Enter the operator you want to use")

    if op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == '*':
        print(num1 * num2)
    elif op == '/':
        print(num1 / num2)
    else:
        print("Invalid operator")

    ch = input("Do you want to continue?")


exp = input("Enter expression")
print(eval(exp))


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


for i in range(0,11):
    print(i)


num = int(input("Enter any number "))

for i in range(1,11):
    print(num," X ", i, " = ", num*i)
li= [1,2,3,44,59,77.83,0.006,"Rachit","Humera21","Nisarg@gmail.com"]
strli=list()
intli=list()
floatli=[]
for i in range(len(li)):
    if type(li[i])==int:
        intli.append(li[i])
    elif type(li[i])==str:
        strli.append(li[i])
    elif type(li[i])== float:
        floatli.append(li[i])


print(strli)
print(intli)
print(floatli)
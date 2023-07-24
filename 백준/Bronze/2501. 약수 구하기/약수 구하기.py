a, b= input().split(" ")
list1=[]

for i in range(1,int(a)//2+1):
    if int(a)% i ==0:
        list1.append(i)
list1.append(int(a))
if len(list1)<int(b):
    print(0)
else:
    print(list1[int(b)-1])

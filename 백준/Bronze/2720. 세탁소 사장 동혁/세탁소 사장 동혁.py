a=int(input())
list1=[]
for i in range(a):
    list1.append(int(input()))
for i in range(len(list1)):
    print(list1[i]//25, list1[i]%25//10,list1[i]%25%10//5,list1[i]%5)

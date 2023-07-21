N,M= input().split(" ")
dex1={}
dex2={}
for i in range(int(N)):
    put=input()
    dex1[i+1]=put
    dex2[put]=i+1
ans=[]
for i in range(int(M)):
    ans.append(input())
for i in ans:
    try:
        i=int(i)
        print(dex1[i])
    except:
        print(dex2[i])
        
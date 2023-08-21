def solution(n, arr1, arr2):
    anslist=[]
    for i in range(n):
        map1=[]
        map2=[]
        answer =""
        while len(map1)<n:
            map1.append(arr1[i]%2)
            arr1[i]=arr1[i]//2
        map1.reverse()
        while len(map2)<n:
            map2.append(arr2[i]%2)
            arr2[i]=arr2[i]//2
        map2.reverse()
        for j in range(n):
            if map1[j]+map2[j]>=1:
                answer+="#"
            else:
                answer+=" "
        anslist.append(answer)

    return anslist
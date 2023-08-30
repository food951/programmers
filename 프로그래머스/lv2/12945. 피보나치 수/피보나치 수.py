def solution(n):
    list1=[0,1]
    for i in range(2,n+1):
        list1.append(list1[i-1]+list1[i-2])
    answer = list1[-1] % 1234567
    return answer
def solution(s):
    n= map(int, s.split())
    list1=list(n)
    maxnum=max(list1)
    minnum=min(list1)
    answer = str(minnum)+" "+str(maxnum)
    
    return answer
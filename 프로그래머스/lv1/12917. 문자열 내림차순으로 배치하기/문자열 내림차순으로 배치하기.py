def solution(s):
    list1=list(s)
    list1.sort(reverse=True)
    
    answer ="".join(list1)
    
    return answer
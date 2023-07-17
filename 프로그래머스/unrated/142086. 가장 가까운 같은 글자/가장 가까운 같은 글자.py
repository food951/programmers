def solution(s):
    answer = []
    dic1 = {}
    
    for i in range(len(s)):
        if s[i] in dic1:
            answer.append(i - dic1[s[i]] )
        else:
            answer.append(-1)
        
        dic1[s[i]] = i
    
    return answer
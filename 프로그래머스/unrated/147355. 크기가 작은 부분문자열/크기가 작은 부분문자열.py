def solution(t, p):
    answer = 0
    t_step= []
    for i in range(len(t) - len(p) + 1):
        t_step.append(t[i:i+len(p)])
    for i in range(len(t_step)) :
        if int(t_step[i]) <= int(p):
            answer +=1
    
    return answer
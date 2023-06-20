def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        answer += absolutes[i] if signs[i] else absolutes[i]*(-1)
#         [True 값] if [조건문] else [False 값]
    
    return answer
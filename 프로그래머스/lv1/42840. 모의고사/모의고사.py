def solution(answers):
    case1 = [1,2,3,4,5]*2000
    case2 = [2,1,2,3,2,4,2,5]*1250
    case3 = [3,3,1,1,2,2,4,4,5,5]*1000
    score = [0,0,0]
    answer = []    
    
    for i in range(len(answers)):
        if answers[i] == case1[i]:
            score[0]+=1;
        if answers[i] == case2[i]:
            score[1]+=1;
        if answers[i] == case3[i]:
            score[2]+=1;
            
    max_score = max(score)
    
    for i in range(len(score)):
        if score[i] == max_score:
            answer.append(i+1)
    answer.sort()
    return answer
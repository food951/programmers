def solution(food):
    answer = '' 
    for i in range(1,len(food)):
        answer += str(i)*(food[i]//2)
    answer += "0"
    for i in range(1,len(food)):
        answer += str(len(food)-i)*(food[len(food)-i]//2)
    return answer
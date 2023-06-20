def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            summ = int(numbers[i])+int(numbers[j]) 
            if summ not in answer :
                answer.append(summ)
    answer.sort()
    return answer
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        div = 0
        for j in range(1,i):
            if i%j ==0:
                div +=1
        if div %2 ==0:
            answer -=i
        else:
            answer+=i
    return answer
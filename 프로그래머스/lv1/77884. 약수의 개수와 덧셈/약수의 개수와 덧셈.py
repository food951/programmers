def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        div = 0
        for j in range(1,i+1):
            if i%j ==0:
                div +=1
        if div %2 ==0:
            answer +=i
        else:
            answer -=i
    return answer
# 모든 제곱수의 약수의 갯수는 홀수, 나머지 수는 짝수이다...

def solution(arr, divisor):
    answer = []
    arr.sort()
    for i in range(len(arr)):
        if arr[i] % divisor ==0:
            answer.append(arr[i])
    if answer ==[]:
        answer=[-1]
    return answer
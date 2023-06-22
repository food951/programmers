def solution(arr):
    total = 0
    for i in range(len(arr)):
        total+= arr[i]
    average = total/len(arr)
    return average
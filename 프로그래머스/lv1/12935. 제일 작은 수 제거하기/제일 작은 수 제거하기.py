def solution(arr):
    
    arr.pop(arr.index(min(arr)))
    if arr==[]:
        arr=[-1]
    
    return arr
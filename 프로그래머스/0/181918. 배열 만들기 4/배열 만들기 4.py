def solution(arr):
    i=0
    stk = []
    while i <len(arr):
        if stk==[] or stk[-1] <arr[i]:
            stk.append(arr[i])
            i+=1
        else: stk.pop()
            
                       
    
    return stk
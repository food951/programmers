def solution(name, yearning, photo):
    result=[0]*len(photo)
    for i in range(len(photo)):
        for j in range(len(name)):
            if name[j] in photo[i]:
                result[i]+=yearning[j]    
    return result
def solution(sizes):
    maxl=0
    maxr=0
    for i in range(len(sizes)):
        if sizes[i][0]<sizes[i][1]:
            sizes[i].reverse()
        maxl=max(sizes[i][0],maxl)
        maxr=max(sizes[i][1],maxr)
    maxsize= maxl*maxr
    return maxsize
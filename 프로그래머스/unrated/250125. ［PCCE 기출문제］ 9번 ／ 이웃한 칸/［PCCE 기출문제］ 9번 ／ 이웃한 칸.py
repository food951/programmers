def solution(board, h, w):
    n=len(board)
    count=0
    select=board[h][w]
    list1= [[h+1,w],[h-1,w],[h,w+1],[h,w-1]]
    for i, j in list1:
        if 0 <= i < n and 0 <= j < n:
            if board[i][j] == select:
                count += 1
    return count
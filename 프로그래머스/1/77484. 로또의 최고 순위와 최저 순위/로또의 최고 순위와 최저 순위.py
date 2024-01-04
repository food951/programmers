def solution(lottos, win_nums):
    count1= 7
    count2= 7
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            count1-=1
            count2-=1
        elif lottos[i]==0:
            count1-=1
            
    if count1==7:
        count1=6
    if count2==7:
        count2=6
    answer = [count1,count2]
    return answer
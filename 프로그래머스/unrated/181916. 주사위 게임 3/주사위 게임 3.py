def solution(a, b, c, d):
    dice = [a, b, c, d]
    dice_counts = [dice.count(i) for i in range(1, 7)]
    
    if 4 in dice_counts:
        p= dice_counts.index(4)+1
        return p*1111
    elif 3 in dice_counts:
        p= dice_counts.index(3)+1
        q= dice_counts.index(1)+1
        return (10*p+q)**2
    elif 2 in dice_counts:
        if 1 in dice_counts:
            q= dice_counts.index(1)+1
            r = dice_counts.index(1, q) + 1
            return q*r
        else : 
            p= dice_counts.index(2)+1
            q= dice_counts.index(2,p)+1
            return (p+q)*abs(p-q)
    else :
        return min(dice)
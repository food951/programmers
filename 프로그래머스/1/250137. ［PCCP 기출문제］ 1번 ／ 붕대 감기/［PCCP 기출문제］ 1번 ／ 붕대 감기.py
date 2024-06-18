def solution(bandage, health, attacks):
    t,x,y = bandage
    full_health =health
    time_list = [item[0] for item in attacks]
    
    last_health=health
    continue_time=0
    for i in range(1,time_list[-1]+1):
        if i in time_list:
            last_health -= attacks[time_list.index(i)][1]
            continue_time= 0
            if last_health <= 0:
                return -1
        else :
            last_health += x
            continue_time+=1
            if continue_time == t:
                last_health+=y
                continue_time =0
            last_health = min(last_health, full_health)
        
            
    
    return last_health
                
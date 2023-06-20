import math
def solution(number, limit, power):
    full_attack =0
    
    for i in range(1,number+1):
        attack = 0    
        sqrt_i=int(math.sqrt(i))
        for j in range(1,sqrt_i+1):
            if i%j ==0:
                attack+=2;
                if j*j==i:
                    attack-=1;
                
        if attack >limit:
            attack = power;
        full_attack += attack
    
    return full_attack
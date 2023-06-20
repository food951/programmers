function solution(number, limit, power) {
    let full_attack = 0;
    for (let i= 1;i<=number;i++){
        let attack = 0; // attack : 공격력값
        for(let j =1;j*j<=i;j++){
            if (i % j == 0){
                attack+=2; // 약수라면 공격력1을 추가,
                if (j*j ==i){
                    attack-=1;
                }
            }
        }
        if (attack >limit){ // 공격력이 limit보다 크면 공격력은 power로 치환
            attack = power 
    
            }
    full_attack += attack;
    }
    
    return full_attack;
}
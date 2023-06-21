function solution(left, right) {
    let answer = 0;
   
    for (let i= left;i<=right;i++){
        let div = 0;

        for (let j = 1;j*j<=i;j++)
            if (i%j ==0){
                div+=2;
                
                if (j*j==i){
                    div -=1
                    
                }}
        if (div %2 ==0){
            answer +=i
        }
        else{
            answer -=i
        }
        
        
        }
    return answer;
}
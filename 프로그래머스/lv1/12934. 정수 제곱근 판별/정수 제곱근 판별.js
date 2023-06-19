function solution(n) {
    let x = Math.floor(Math.sqrt(n));
    if(x * x == n)  {
        return (x + 1) ** 2
    }
    else{  
        return -1}
}
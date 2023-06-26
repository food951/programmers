function solution(num_list) {
   
    if (num_list.length >=11){
        let total= 0
        for(let i=0;i<num_list.length;i++){
            total += num_list[i]
        }
        return total
    }
    else{
        let mul = 1
        for(let i=0;i<num_list.length;i++){
            mul *= num_list[i]
        }
        return mul
    }
}
   
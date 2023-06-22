function solution(answers) {
    let case1 = Array(2000).fill([1,2,3,4,5]).flat();
    let case2 = Array(1250).fill([2,1,2,3,2,4,2,5]).flat();
    let case3 = Array(1000).fill([3,3,1,1,2,2,4,4,5,5]).flat();
    let score = [0,0,0]
    var answer = [];
    for(let i=0;i<answers.length;i++){
        if (case1[i]==answers[i]){
            score[0]+=1;}
        if (case2[i]==answers[i]){
            score[1]+=1;}
        if (case3[i]==answers[i]){
            score[2]+=1;}
    }
    let max_score = Math.max(...score)
    for(let i =0;i<3;i++){
        if (max_score == score[i]){
            answer.push(i+1)
        }
    }
   
    return answer;
}
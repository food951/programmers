function solution(a, b) {
    let date = [31,29,31,30,31,30,31,31,30,31,30,31]
    let day= 0
    let week ={0:"THU", 1:"FRI",2:"SAT",3:"SUN",4:"MON",5:"TUE",6:"WED"}
    for (let i = 1;i<a;i++){
        day +=date[i-1]
    }
    day= day+b
    
    var answer = week[day%7];
    return answer;
}
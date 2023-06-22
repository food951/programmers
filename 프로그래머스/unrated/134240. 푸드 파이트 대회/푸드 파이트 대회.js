function solution(food) {
    var answer = "";
    
    for (var i = 1; i <= food.length; i++) {
        answer += String(i).repeat(parseInt(food[i]/2));
    }
    
    answer += "0".repeat(parseInt(food[0]));
    
    for (var i = food.length; i >= 1; i--) {
        answer += String(i).repeat(parseInt(food[i]/2));
    }
    
    return answer;
}
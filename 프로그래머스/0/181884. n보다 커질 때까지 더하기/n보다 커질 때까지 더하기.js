function solution(numbers, n) {
    var answer = 0;
    for (let el of numbers) {
        answer += el
        
        if(answer > n) break;
    }
    
    return answer;
}
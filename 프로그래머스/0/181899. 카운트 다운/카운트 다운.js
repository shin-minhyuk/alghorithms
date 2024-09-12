function solution(start_num, end_num) {
    var answer = [];
    
    for(let i = start_num; i>end_num; i--) {
        if (i === start_num) {
            answer.push(i)
        }
        answer.push(i-1)
    }
    
    return answer;
}
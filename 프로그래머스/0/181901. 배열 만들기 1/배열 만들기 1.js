function solution(n, k) {
    var answer = [];
    for(let i =1; i <= parseInt(n/k); i++) {
        answer.push(i * k)
    }
    return answer
}
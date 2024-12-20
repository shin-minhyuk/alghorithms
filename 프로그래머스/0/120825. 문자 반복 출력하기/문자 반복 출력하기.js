function solution(my_string, n) {
    let answer = []
    my_string.split("").forEach(el => {
        for(let i = 0; i < n; i++) {
            answer.push(el)
        }
    })
    return answer.join('').toString()
}
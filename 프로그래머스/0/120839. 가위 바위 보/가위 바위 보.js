function solution(rsp) {
    const answer = rsp.split("").map(el => el === "2" ? "0" : el === "0" ? "5" : el === "5" ? "2" : null)
    
    return answer.join("")
}
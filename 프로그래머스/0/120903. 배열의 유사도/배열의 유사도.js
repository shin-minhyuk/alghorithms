function solution(s1, s2) {
    let i = 0
    s1.forEach(el => s2.forEach(element => element === el ? i++ : null))
    return i
}
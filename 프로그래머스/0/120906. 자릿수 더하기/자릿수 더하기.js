function solution(n) {
    let arr = []
    n.toString().split("").forEach(v => arr.push(parseInt(v)))

    let num = 0
    arr.forEach(v => num += v)
    return num
}
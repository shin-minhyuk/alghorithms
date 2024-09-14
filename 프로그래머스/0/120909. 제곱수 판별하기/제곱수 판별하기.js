function solution(n) {
    var answer = Math.sqrt(n)
    if (Number.isInteger(answer)) {
        return 1
    } else {
        return 2
    }
}

// n이 거듭제곱이면 1 아니면 2
// Math.sqrt(n)
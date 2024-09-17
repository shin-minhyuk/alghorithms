function solution(number, n, m) {
    // number가 n과 m의 공배수 ? 1 : 0
    if (number / n === parseInt(number / n)) {
        if (number / m === parseInt (number / m)) {
            return 1
        } else {
            return 0
        }
    } else {
        return 0
    }
}
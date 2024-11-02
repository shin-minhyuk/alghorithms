function solution(money) {
    const coffee = 5500
    if (money >= 5500) {
        return [Math.floor(money / coffee), money % coffee]
    }
    return [0, money]
}
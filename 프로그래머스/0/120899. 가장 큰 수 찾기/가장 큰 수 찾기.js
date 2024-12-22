function solution(array) {
    const big = Math.max(...array)
    
    return [big, array.indexOf(big)]
}
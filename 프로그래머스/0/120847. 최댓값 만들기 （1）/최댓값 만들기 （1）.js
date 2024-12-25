function solution(numbers) {
    const arr = numbers.sort(function(a,b) {
        return b-a
    } )
    
    return arr[0] * arr[1]
}
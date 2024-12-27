function solution(my_string) {
    let result = 0
    const arr = my_string.split("")
    arr.forEach(el => {
        if(Number(el)) {
            result += Number(el)
        }
    })
    return result
}
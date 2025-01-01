function solution(my_string) {
    const stringArr = my_string.split("")
    let newArr = []
    stringArr.forEach((el) => {
        if(el === el.toUpperCase()) {
            return newArr.push(el.toLowerCase())
        }
        
        if (el === el.toLowerCase()) {
            return newArr.push(el.toUpperCase())
        }
        return null
    })
    
    return newArr.join("")
}
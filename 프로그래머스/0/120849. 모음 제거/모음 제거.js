let arr = ["a", "e", "i", "o", "u"]

function solution(str) {
    let newArr = []
    str.split("").forEach(el => {
        if(!arr.includes(el)) {
            newArr.push(el)
        }
    })
    
    return newArr.join("")
}
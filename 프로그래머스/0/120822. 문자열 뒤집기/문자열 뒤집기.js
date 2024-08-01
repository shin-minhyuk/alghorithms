function solution(my_string) {
    var answer = my_string.split("").reverse().join("")
    return answer;
}

// function solution(my_string) {
//     var answer = '';
//     for (let i = my_string.length - 1; i >= 0; i -= 1)
//         answer += my_string[i]
//     return answer;
// }
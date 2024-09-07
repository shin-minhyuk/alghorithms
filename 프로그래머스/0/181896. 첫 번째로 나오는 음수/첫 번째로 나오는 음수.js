const solution = (num_list) => {
    let result
    result = num_list.findIndex((el) => el<0)
    return result
}  

//첫 번째로 나오는 음수의 인덱스
//없으면 -1
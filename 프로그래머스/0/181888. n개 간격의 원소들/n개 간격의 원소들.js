function solution(num_list, n) {
    // n번째 마다 배열에 넣어야함 [0, n, 2n, 3n, 4n]                    
    return num_list.filter((el, idx) => idx % n === 0)
}
function solution(num_list, n) {
    var answer = [];
    // n번째 마다 배열에 넣어야함 [0, n, 2n, 3n, 4n]
    answer = num_list.filter((el, idx) => idx % n === 0)
                    
    return answer;
}
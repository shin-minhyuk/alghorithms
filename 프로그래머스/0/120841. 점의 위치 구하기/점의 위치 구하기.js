function solution(dot) {
    
    if (dot[0] > 0 && dot[1] > 0) return 1
    if (dot[0] < 0 && dot[1] > 0) return 2
    if (dot[0] < 0 && dot[1] < 0) return 3
    if (dot[0] > 0 && dot[1] < 0) return 4
    
    return alert("이것도 아니고 저것도 아니면 버그임")
}
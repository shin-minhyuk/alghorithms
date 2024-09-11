const solution = (n, k) => {
    let result;
    if (n >= 10) {
        const serviceJuice = Math.floor(n / 10)
        result = ((12000*n)+(2000*k)-(2000*serviceJuice)) 
    } else {
        result = (12000*n)+(2000*k)
    }
    
    return result
}
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    
    let arr = []
    for (let el of str) {
        el === el.toUpperCase() ? arr.push(el.toLowerCase()) : arr.push(el.toUpperCase())
    }
    console.log(arr.join(""))
    
});
function solution(n) {
    var answer = [];
    answer=String(n).split('');
    var arr= [];
    //console.log(answer);
    for(let i=0; i<answer.length; i++){
        arr.push(Number(answer[i]))
    }
    var result = arr.reverse();
    return result;
}
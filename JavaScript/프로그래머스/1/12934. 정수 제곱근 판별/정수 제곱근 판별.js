function solution(n) {
    var answer = Math.sqrt(n);
    var result = 0;
    if(Number.isInteger(answer)){
        result=(answer+1)*(answer+1)
    }
    else{
        result=-1
    }
    return result;
}
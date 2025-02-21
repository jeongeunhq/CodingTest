function solution(numbers) {
    var sum = 0;
    for(var i=0; i<numbers.length; i++){
        sum+=numbers[i]
    }
    var answer=sum/numbers.length
    return answer;
}
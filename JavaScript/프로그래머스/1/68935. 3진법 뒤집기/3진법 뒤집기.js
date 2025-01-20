function solution(n) {
    var answer = 0;
    let change=n.toString(3)
    const changeReverse=change.split("").reverse().join("")
    answer=parseInt(changeReverse,3)
    return answer;
}
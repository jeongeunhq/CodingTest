function solution(n)
{
    var answer = 0;
    const str=n.toString();
    const arr=str.split('');
    for(var i=0; i<arr.length; i++){
        var num=Number(arr[i])
        answer+=num
    }
    return answer;
}
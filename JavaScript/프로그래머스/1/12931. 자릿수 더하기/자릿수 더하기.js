function solution(n)
{
    var answer = 0;
    const arr=String(n).split('');
    for(var i=0; i<arr.length; i++){
        answer+=Number(arr[i])
    }


    return answer;
}
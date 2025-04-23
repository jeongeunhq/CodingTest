function solution(s) {
    var answer = '';
    const len=s.length;
    let mid = Math.floor(len/2);
    if(len%2==0){
        answer=s[mid-1]+s[mid];
    }
    else{
        answer+=s[mid]
    }
    return answer;
}
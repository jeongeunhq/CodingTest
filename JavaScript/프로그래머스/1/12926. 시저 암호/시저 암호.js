function solution(s, n) {
    var answer = '';
    for(let i=0; i<s.length; i++){
        let Ascill = s.charCodeAt(i)
        if(Ascill>=65 && Ascill<=90){
            Ascill+=n
            if(Ascill>90){
                Ascill-=26
            }
        }
        else if(Ascill>=97 && Ascill<=122){
            Ascill+=n
             if(Ascill>122){
                Ascill-=26
            }
        }
        let str=String.fromCharCode(Ascill)
        answer+=str
    }
    
    return answer;
}
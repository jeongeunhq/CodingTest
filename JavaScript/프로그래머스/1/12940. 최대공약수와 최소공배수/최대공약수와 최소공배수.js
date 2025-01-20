function solution(n, m) {
    var answer = [];
    a=Math.max(n,m);
    b=Math.min(n,m);
    
    for(var i=b; i>=1; i--){
        if(n%i==0&&m%i==0){
            return [i, (n*m)/i]
        }
    }
    return answer;
}
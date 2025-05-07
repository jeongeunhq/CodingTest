let getGCD = (n,m) =>{
    let gcd = 1;
    for(let i=2; i<=Math.min(n,m); i++){
        if(n%i===0 && m%i===0){
            gcd=i;
        }
    }
    return gcd;
}

let getLCM = (n,m) => {
    let lcm = 1;
    while(true){
        if((lcm % n==0)&&(lcm%m==0)){
            break;
        }
        lcm++;
    }
    return lcm;
}

function solution(n, m) {
    var answer = [];
    answer.push(getGCD(n,m));
    answer.push(getLCM(n,m));
    return answer;
}
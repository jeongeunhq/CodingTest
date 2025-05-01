function solution(price, money, count) {
    var cal = 0;
    var ans = 0;
    for(let i=1; i<=count; i++){
        cal+=price*i
    }
    ans=cal-money;
    if(ans<=0){
        ans=0;
    }

    return ans;
}
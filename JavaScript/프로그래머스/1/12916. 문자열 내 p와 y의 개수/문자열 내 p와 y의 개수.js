function solution(s){
    var answer = true;
    const arr = s.toLowerCase();
    var a=0;
    var b=0;
    //console.log(arr);
    for(var i=0; i<arr.length; i++){
       if(arr[i]=='p'){
           a+=1;
       }
        else if(arr[i]=='y'){
            b+=1;
        }
    }
    if(a==b){
        answer=true;
    }
    else{
        answer=false;
    }

    return answer;
}
function solution(my_string, letter) {
    var answer = [];
    for(var i=0; i<my_string.length; i++){
        let str=my_string[i]
        if(str===letter){
            continue;
        }
        else{
            answer.push(str)
        }
    }
    return answer.join("");
}
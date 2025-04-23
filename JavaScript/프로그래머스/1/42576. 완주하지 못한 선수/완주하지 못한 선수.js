function solution(participant, completion) {
    const map = new Map();
    for(let x of participant){
        map.set(x, (map.get(x) || 0) + 1);
    }
    for(let x of completion){
        map.set(x, (map.get(x) || 0) - 1);
    }
    for(let[k,v] of map){
        if(v==1){
            return k;
        }
    }
   
}
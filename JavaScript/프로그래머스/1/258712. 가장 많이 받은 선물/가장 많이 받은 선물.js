function solution(friends, gifts) {
    var answer = 0;
    //선물 기록
    const records = Array.from(Array(friends.length), ()=> Array(friends.length).fill(0));
    //선물 지수
    const giftScore = Array(friends.length).fill(0);
    
    //선물 기록 및 선물 지수 계산
    gifts.forEach(gift =>{
        const [giver, receiver] = gift.split(' ');
        const giveIndex = friends.indexOf(giver);
        const receiveIndex = friends.indexOf(receiver);
        
        records[giveIndex][receiveIndex]++;
        giftScore[giveIndex]++;
        giftScore[receiveIndex]--;
    });
    
    //다음 달에 받을 선물 계산
    const next = Array(friends.length).fill(0);
    
    for(let i=0; i<friends.length; i++){
        for(let j=i+1; j<friends.length; j++){
            if(records[i][j]>records[j][i]){
                next[i]++;
            }
            else if(records[i][j]<records[j][i]){
                next[j]++;
            }
            else{
                if(giftScore[i]>giftScore[j]){
                    next[i]++;
                }
                else if(giftScore[i]<giftScore[j]){
                    next[j]++;
                }
            }
        }
    }
    answer=Math.max(...next);
    return answer;
}
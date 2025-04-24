function solution(array, commands) {
    var arr = [];
    for(var i=0; i<commands.length; i++){
        var sliced = array.slice(commands[i][0]-1,commands[i][1]);
        sliced.sort((a,b)=>a-b);
        var k = commands[i][2]-1
        arr.push(sliced[k])
}
    return arr;
}
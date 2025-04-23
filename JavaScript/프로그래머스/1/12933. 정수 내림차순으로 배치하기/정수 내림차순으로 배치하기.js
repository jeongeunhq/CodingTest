function solution(n) {
    var nString = String(n);
    var arr = nString.split('').sort((a, b) => b - a).join("");
    //console.log(arr);
    return parseInt(arr);
}
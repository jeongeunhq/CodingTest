def solution(participant, completion):
    
    hashdic={}
    hashSum=0
    for par in participant:
        hashdic[hash(par)]=par
        hashSum+=hash(par)
    for com in completion:
        hashSum-=hash(com)
        
    return hashdic[hashSum]
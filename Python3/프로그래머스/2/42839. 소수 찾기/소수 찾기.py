from itertools import permutations

def prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

def solution(numbers):
    answer = 0
    num=[]
    for i in range(1,len(numbers)+1):
        num.append(list(set(map(''.join, permutations(numbers, i)))))
    per = list(set(map(int, set(sum(num, [])))))   
    
    for i in per:
        if prime(i)==True:
            answer+=1
    return answer
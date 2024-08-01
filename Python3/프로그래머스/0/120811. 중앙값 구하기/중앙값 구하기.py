def solution(array):
    array.sort()
    a=len(array)//2
    a=int(a)
    answer = array[a]
    return answer
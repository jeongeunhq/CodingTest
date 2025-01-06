def solution(nums):
    answer = 0
    remove=set(nums)
    if len(remove)>len(nums)/2:
        answer=len(nums)/2
    else:
        answer=len(remove)
    return answer
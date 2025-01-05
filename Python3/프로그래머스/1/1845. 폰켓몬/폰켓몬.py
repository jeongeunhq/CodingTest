def solution(nums):
    answer = 0
    choice=set(nums)
    if len(nums)/2 > len(choice):
        answer=len(choice)
    else:
        answer=len(nums)/2
    return answer
    
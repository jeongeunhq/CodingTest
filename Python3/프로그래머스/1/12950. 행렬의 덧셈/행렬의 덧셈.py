def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer_sum=[]
        for j in range(len(arr1[0])):
            answer_sum.append(arr1[i][j]+arr2[i][j])
        answer.append(answer_sum)
    return answer
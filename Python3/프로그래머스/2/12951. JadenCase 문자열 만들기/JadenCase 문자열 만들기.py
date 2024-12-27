def solution(s):
    answer = []
    list_s=s.split(' ')
    for i in range(len(list_s)):
        list_s[i]=list_s[i][:1].upper()+list_s[i][1:].lower()
    answer=(' ').join(list_s)
    return answer
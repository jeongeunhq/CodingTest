def solution(s):
    # 문자열을 모두 소문자로 변환
    s = s.lower()
    
    # 'p'와 'y'의 개수를 세기
    count_p = s.count('p')
    count_y = s.count('y')
    
    # 'p'와 'y'의 개수가 같으면 True, 다르면 False 반환
    return count_p == count_y

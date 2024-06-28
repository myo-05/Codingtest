def solution(s, n):
    if n < 1 or n > 25:
        return 0
    lower= 'abcdefghijklmnopqrstuvwxyz'
    upper = lower.upper()
    
    answer = ''
    for s_ in s:
        if s_ == " ": # 공백이라면
            answer += " "
        elif s_ == s_.lower() : # 소문자라면
            answer += lower[(lower.index(s_)+n) % len(lower)]
        else : # 대문자라면
            answer += upper[(upper.index(s_)+n) % len(lower)]
    return answer
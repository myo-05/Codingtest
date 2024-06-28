def solution(s):
    answer = ''
    odd = True
    for i in s:
        if i == " ":
            answer += i
            odd = True
            continue
        if odd:
            answer += i.upper()
            odd = False
        else:
            answer += i.lower()
            odd = True
    return answer
def solution(my_string):
    answer = 0
    tmp = ''
    for s in my_string:
        if s.isdigit():
            tmp += s
        elif tmp:
            answer += int(tmp)
            tmp = ''
    if tmp:
        answer += int(tmp)
    return answer
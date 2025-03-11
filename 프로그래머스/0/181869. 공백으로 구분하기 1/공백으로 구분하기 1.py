def solution(my_string):
    answer = []
    tmp = ''
    for s in my_string:
        if s == ' ':
            answer.append(tmp)
            tmp = ''
        else:
            tmp += s
    answer.append(tmp)
    return answer
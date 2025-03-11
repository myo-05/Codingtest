def solution(my_string):
    answer = []
    word = ''
    for i,s in enumerate(my_string):
        if s == ' ' and word != '':
            answer.append(word)
            word =  ''
        if s != ' ':
            word += s
    if word != '':
        answer.append(word)
    return answer
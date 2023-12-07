def solution(s, skip, index):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''
    for j in skip:
        if j in alphabet:
            alphabet = alphabet.replace(j,'')
    for i in s:
        n = alphabet[(alphabet.index(i) + index)%len(alphabet)]
        answer += n
    return answer
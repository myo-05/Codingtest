def solution(cipher, code):
    answer = ''
    for i,s in enumerate(cipher,1):
        if i%code == 0:
            answer += s
    return answer
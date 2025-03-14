def solution(picture, k):
    answer = []
    for pixel in picture:
        tmp = ''
        for p in pixel:
            tmp += p*k
        for _ in range(k):
            answer.append(tmp)
    return answer
def solution(order):
    answer = 0
    for n in str(order):
        if int(n) in (3,6,9):
            answer += 1
    return answer
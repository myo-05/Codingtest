def solution(a, b):
    answer = [abs(a-b), 2*(a+b), a**2+b**2]
    return answer[int(a%2)+int(b%2)]

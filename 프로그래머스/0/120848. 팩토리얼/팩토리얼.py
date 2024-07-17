def factorial(x):
    if x == 1:
        return 1
    return factorial(x-1)*x

def solution(n):
    answer = 1
    while n > factorial(answer):
        answer += 1
    if n < factorial(answer):
        answer -= 1
    return answer
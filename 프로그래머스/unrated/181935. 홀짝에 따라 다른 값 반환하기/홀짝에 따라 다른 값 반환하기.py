def solution(n):
    answer = 0
    if n % 2 == 1 : #홀수라면
        for odd in range(1,n+1,2):
            answer += odd
    else : #짝수라면
        for even in range(0,n+1,2):
            answer += even**2
    return answer
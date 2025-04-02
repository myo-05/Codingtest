def solution(n):
    return sum(int(n%i==0) for i in range(1,n+1))
# 리팩토링 코드 | 다중할당 , for, range , 나머지 연산자 사용
def solution(n):
    f0,f1=0,1
    for _ in range(n):
        f0, f1 = f1, (f0+f1)%1234567
    return f0
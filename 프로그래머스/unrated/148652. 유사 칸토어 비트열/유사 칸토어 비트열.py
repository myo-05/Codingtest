# 새로운풀이 - 일반화

def bitcount(n,x): # 처음부터 x번째 까지의 1의 개수를 구하는 함수
    if x == 0:
        return 0
    if n == 0: 
        return 1
    count = 4**(n-1) # # 이전 bit열의 1의 총 개수
    lenth = 5**(n-1) # 이전 bit열의 전체길이
    a = x//lenth # 이전 bit열의 개수에 곱할 몫
    b = x%lenth # 남은 카운팅 인덱스
    if a==2:
        return count*a
    if a >= 3:
        a = a-1
    return count*a + bitcount(n-1,b)

def solution(n, l, r):
    print(bitcount(n,r))
    return bitcount(n,r)-bitcount(n,l-1)
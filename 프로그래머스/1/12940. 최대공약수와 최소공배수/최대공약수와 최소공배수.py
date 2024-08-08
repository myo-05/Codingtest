def solution(n, m):
    answer = []
    n, m = min(n,m), max(n,m)
    for i in range(n,0,-1): #큰 수부터
        if n % i == 0 and m % i == 0: #공약수라면
            answer.append(i) # 최대공약수 추가
            answer.append(n*m/i) # 최소공배수 추가
            break
    return answer
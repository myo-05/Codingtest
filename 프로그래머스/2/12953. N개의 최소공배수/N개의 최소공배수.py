def solution(arr):
    answer = 0
    m = arr[0]
    for n in arr:
        min_n = min(n,m)
        for i in range(min_n,0,-1): #큰 수부터 역순
            if n % i == 0 and m % i == 0: #공약수라면
                answer = int(n*m/i) # 최소공배수 저장
                m = answer
                break
    return answer
def solution(n):
    answer = 0
    for i in range(n):
        sum = 0 # 합
        while sum < n: # 합이 n보다 작다면 수행
            i += 1 # 연속수 증가
            sum += i # 합산
            if sum == n: # 합이 n과 일치하면 카운트
                answer += 1
    return answer

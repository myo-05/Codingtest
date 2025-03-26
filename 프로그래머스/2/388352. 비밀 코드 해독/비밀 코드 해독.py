import itertools

def solution(n, q, ans):
    pw_len = 5
    answer = 0 # 적용 케이스
    numbers = [i for i in range(1,n+1)] # 정수범위
    comb_case = itertools.combinations(numbers,pw_len) # 모든 조합
    
    for comb in comb_case:
        for request,respons in zip(q,ans):
            match_count = len(set(comb)&set(request)) # 일치수
            if match_count != respons: # 일치수와 응답이 다르다면
                break # 탈락
        else: # 모두 일치하면
            answer += 1 # 케이스 추가
    return answer
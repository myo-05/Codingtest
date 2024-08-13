'''
서로 다른 종류의 수를 최소화
귤의 개수 k
귤의 크기를 담은 배열 tangerine
'''
# 초기풀이 - 시간초과
# def solution(k, tangerine):
#     answer = 0 # 서로 다른 종류의 수의 최솟값
#     tmp=[tangerine.count(i) for i in set(tangerine)] # 종류별 개수 저장
#     tmp.sort(reverse=True) # 내림차순 정렬
#     for j in tmp: # 개수가 많은 종류부터 선택
#         k -= j # 포장수량에서 제거
#         answer += 1 # 종류 카운트
#         if k <= 0: # 포장수량이 충족됐다면 가짓수 반환
#             return answer
    
# 리팩토링 - dict 사용
def solution(k, tangerine):
    answer = 0 # 서로 다른 종류의 수의 최솟값
    tmp = {}
    for i in tangerine: # 종류별 개수 저장
        try:
            tmp[i] += 1
        except:
            tmp[i] = 1
    tmp = list(tmp.values()) # 종류별 개수
    tmp.sort(reverse=True) # 내림차순 정렬
    for j in tmp: # 개수가 많은 종류부터 선택
        k -= j # 포장수량에서 제거
        answer += 1 # 종류 카운트
        if k <= 0: # 포장수량이 충족됐다면 가짓수 반환
            return answer
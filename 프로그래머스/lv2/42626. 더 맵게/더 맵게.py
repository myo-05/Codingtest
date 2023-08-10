import heapq
def solution(scoville, K):
    if K == 0  or min(scoville) >= K: # 처음부터 충족할 경우
        return 0
    heapq.heapify(scoville)
    count = 0
    while True :
        count += 1 # 횟수 추가
        heapq.heappush(scoville,heapq.heappop(scoville)+heapq.heappop(scoville)*2) # 음식 섞기
        if scoville[0] >= K: # 최소 스코빌 지수가 K 이상이라면 while문 탈출
            break
        if len(scoville) == 1 and scoville[0] < K: # 음식이 하나일 때도 스코빌 지수가 낮다면
            return -1
    return count
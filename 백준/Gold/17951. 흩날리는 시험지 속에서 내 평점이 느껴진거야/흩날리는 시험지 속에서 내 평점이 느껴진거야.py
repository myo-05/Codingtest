import sys
input = sys.stdin.readline

N,K = map(int,input().split()) # 시험지, 그룹 수
x_list = list(map(int,input().split())) # 시험지의 점수

s = start = min(x_list) # 최소 점수
e = end = sum(x_list) # 최대 점수

while s <= e:
    mid = (s + e)//2 # 목표값(최대합)
    groups = 0    
    score = 0 # 점수합
    for i in range(N):
        score += x_list[i]
        if mid <= score: # 목표값에 도달하면
            groups +=1 # 그룹구분
            score = 0 # 점수합 초기화
    if groups >= K: # 목표 그룹수가 크다면 목표값 늘리기
        s = mid + 1
    elif groups < K: # 목표 그룹수가 작다면 목표값 줄이기
        e = mid - 1
print(e)
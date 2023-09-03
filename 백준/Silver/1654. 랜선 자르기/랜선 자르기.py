import sys
input = sys.stdin.readline

K,N = map(int,input().split()) # 기존랜선 수, 목표랜선 수
lines = [int(input()) for _ in range(K)] # 랜선길이

s = start = 1 # 최소 최대랜선길이
e = end = max(lines) # 최대 최대랜선길이

while s <= e:
    mid = (s + e) // 2 # 목표값(최대랜선길이)
    count = 0 # 랜선 수
    for line in lines:
        count += line//mid
    if count >= N : # 목표랜선 수보다 크면 목표값을 높인다
        s = mid + 1
    elif count < N : # 목표랜선 수보다 작으면 목표값을 낮춘다
        e = mid - 1
print(e)
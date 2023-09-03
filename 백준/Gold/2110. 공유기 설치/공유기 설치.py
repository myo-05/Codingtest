import sys

input = sys.stdin.readline
N, C = map(int,input().split())
houses = []

for _ in range(N):
    x = int(input())
    houses.append(x)
houses.sort() # 정렬

s = start = 1                  # 최소거리
e = end = houses[-1]-houses[0] # 최대거리

while s <= e:
    mid = (s+e)//2 # 목표거리
    router = 1 # 공유기 *기본적으로 처음 집에 설치
    last_installed_idx = 0 # 현재 마지막에 설치된 집 
    for i in range(1,N):
        if mid <= houses[i]-houses[last_installed_idx] : # 목표거리를 충족하면
            router += 1 # 공유기 놓기
            last_installed_idx = i # 마지막 설치된 집 업데이트
    if router >= C : # 조건의 공유기 수보다 많다면 목표거리를 늘려주자
        s = mid + 1
    elif router < C : # 조건의 공유기 수보다 적다면 목표거리를 줄여주자
        e = mid - 1
print(e)
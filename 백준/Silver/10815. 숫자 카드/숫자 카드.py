import sys
input = sys.stdin.readline

N = int(input()) # 가진 카드 수
cards = list(map(int,input().split())) # 가진 카드들
M = int(input()) # 확인 카드 수
checks = list(map(int,input().split())) # 확인 카드들

cards.sort() # 이진탐색 전 정렬
answer = []

for check in checks:
    s = start = 0 # 최소 index 
    e = end = N-1 # 최대 index
    while s <= e:
        mid = (s + e)//2 # 목표인덱스
        if cards[mid] > check: # 탐색숫자보다 크다면 인덱스 낮추기
            e = mid - 1
        elif cards[mid] <= check: # 탐색숫자보다 작다면 인덱스 높이기
            s = mid + 1
    answer.append('1' if cards[e] == check else '0') # 판별결과 저장
print(' '.join(answer))
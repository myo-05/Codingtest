import sys
input = sys.stdin.readline

N = int(input()) # 가진 카드 수
cards = set(map(int,input().split())) # 가진 카드들
M = int(input()) # 확인 카드 수
checks = list(map(int,input().split())) # 확인 카드들

for check in checks:
    print(1,end=" ") if check in cards else print(0,end=" ") 
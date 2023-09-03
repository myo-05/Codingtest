import sys
from collections import Counter
input = sys.stdin.readline

N = int(input()) # 가진 카드 수
cards = list(map(int,input().split())) # 가진 카드들
M = int(input()) # 확인 카드 수
checks = list(map(int,input().split())) # 확인 카드들

cards = Counter(cards)

for check in checks:
    try:
        print(cards[check],end=" ")
    except:
        print(0,end=" ")
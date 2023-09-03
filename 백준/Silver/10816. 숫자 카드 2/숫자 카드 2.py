import sys
from collections import Counter
input = sys.stdin.readline

N = int(input()) # 가진 카드 수
cards = list(map(int,input().split())) # 가진 카드들
M = int(input()) # 확인 카드 수
checks = list(map(int,input().split())) # 확인 카드들

cards = Counter(cards)

print(' '.join(str(cards[check]) if check in cards else '0' for check in checks))
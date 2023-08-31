import sys
input = sys.stdin.readline
from collections import Counter

M, N = map(int,input().split())
A_list = Counter(map(int,input().split())) # 중복값고려

count = 0
s = start = 0
e = end = 1000000**2
while s <= e:
    time = (s + e)//2
    count = sum(time//Ai*i for Ai,i in A_list.items())
    if count < N: # 풍선이 부족하다
        s = time+1 # 시간을 늘린다
    elif count >= N: # 풍선이 충분하다
        e = time-1 # 시간을 줄인다
print(s)
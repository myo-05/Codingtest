import sys

input = sys.stdin.readline
N,M = map(int,input().split()) # 나무의 수, 나무의 길이

trees = list(map(int,input().split())) # 나무들의 높이

low = 0 # 바닥
high = max(trees) # 가장높은 나무의 길이

while low <= high:
    mid = (low + high) // 2
    H = mid # 절단높이

    cut_len = 0 # 절단 후 가져가게되는 길이

    for tree in trees:
        if tree > H :
            cut_len += tree - H

    if cut_len == M:
        high = H
        break
    elif cut_len >= M : # 많이 잘랐다
        low = H+1 # 더 높이 자르기
    elif cut_len < M : # 덜 잘랐다
        high = H-1 # 더 낮게 자르기
print(high)
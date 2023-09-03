import sys
input = sys.stdin.readline

N = int(input()) # 용액의 수
solutions = list(map(int,input().split())) # 용액특성

solutions.sort() # 특성 정렬

s = start = 0 # 최소 index
e = end = N-1 # 최대 index
min_solution = 2*10**9

while s < e:
    mix = solutions[s]+solutions[e]
    if abs(mix) < min_solution:
        min_solution = abs(mix)
        answer=[solutions[s],solutions[e]]
    if mix == 0:
        break
    elif mix > 0:
        e -= 1
    else:
        s += 1
print(*answer,end=" ")
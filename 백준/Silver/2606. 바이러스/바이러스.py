import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline
N = int(input()) # 컴퓨터 수
M = int(input()) # 연결된 수
V = 1 # 감염된 컴퓨터 번호

graph = defaultdict(list)

for _ in range(M): # 그래프만들기
    node1,node2 = map(int,input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

def BFS(graph, start):
    visited = [start]
    q = deque([start])

    while q:
        node = q.popleft()
        for adj in graph[node]:
            if adj not in visited:
                q.append(adj) # 동일 level 방문예약
                visited.append(adj) # 방문처리
    print(len(visited)-1) # 1번 제외 총 감염 수

BFS(graph,1)
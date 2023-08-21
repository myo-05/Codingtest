import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline
N,M,V = map(int,input().split()) # 정점 수(N), 간선 수(M), 탐색시작정점번호(V)

graph = defaultdict(list)

for _ in range(M): # 그래프만들기
    node1,node2 = map(int,input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

def DFS(graph,node,visited):
    # 방문처리
    visited.append(node)
    print(node,end=" ")
    # 인접 노드 방문
    for adj in sorted(graph[node]): # 작은 것 우선 방문
        if adj not in visited:
            DFS(graph, adj, visited) # 다음 level 방문


def BFS(graph, start):
    visited = [start]
    q = deque([start])

    while q:
        node = q.popleft()
        print(node,end=" ")
        for adj in sorted(graph[node]): # 작은 것 우선 방문
            if adj not in visited:
                q.append(adj) # 동일 level 방문예약
                visited.append(adj) # 방문처리

DFS(graph,V,[])
print()
BFS(graph,V)
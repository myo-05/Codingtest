import heapq
import sys
input = sys.stdin.readline
n = int(input())

answer = []
heap = []
heapq.heapify(heap)
for _ in range(n):
    order = int(input())
    if order > 0:
        heapq.heappush(heap,-order)
    elif order == 0:
        answer.append(str(-heapq.heappop(heap)) if heap else '0')
print('\n'.join(answer))
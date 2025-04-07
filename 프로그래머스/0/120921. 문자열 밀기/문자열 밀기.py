from collections import deque

def solution(A, B):
    answer = 0
    a = deque(s for s in A)
    b = deque(s for s in B)
    for _ in A:
        if a == b:
            break
        answer += 1
        a.rotate(1)
    else:
        return -1
        
    return answer
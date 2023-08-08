from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    stack = deque([0]*bridge_length)
    sum_stack = 0
    while stack: # 다리 위 트럭이 존재한다면 반복
        time += 1
        check = stack.pop() # 트럭이동
        if check > 0:
            sum_stack -= check

        if truck_weights: # 대기트럭이 존재한다면
            if sum_stack+truck_weights[0]>weight: # 무게가 초과한다면
                stack.appendleft(0) # 그냥이동
            else:                                   # 무게가 초과하지 않으면
                add = truck_weights.pop(0)
                stack.appendleft(add) # 트럭추가
                sum_stack += add
    return time
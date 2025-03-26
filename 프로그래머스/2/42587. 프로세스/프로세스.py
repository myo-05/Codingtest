def solution(priorities, location):
    answer = 0
    queue = [[idx,priority] for idx,priority in enumerate(priorities)] # 인덱스(프로세스명),우선순위 저장
    while queue:
        # 1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
        current = queue.pop(0)
        # 2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
        if any(current[1] < wait[1] for wait in queue):
            queue.append(current)
        # 3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
        else: # 3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.
            answer += 1 # 실행 카운트
            # 타겟 프로세스라면 반환
            if current[0] == location:
                return answer
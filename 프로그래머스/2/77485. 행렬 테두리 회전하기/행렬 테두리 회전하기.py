# 시간복잡도 개선 - 리스트컴프리헨션 / deepcopy→직접변환 / min→최솟값대조
def solution(rows, columns, queries):
    # (1) 최초 행렬생성
    # (2) query마다 좌표 인식 후 해당 행렬값 변경 후 저장
    # (3) 변경되는 좌표 중 min값 answer 저장
    # 반복 후 출력
    answer = []
    matrix = [[(i-1)*columns + j for j in range(1,columns+1)]for i in range(1,rows+1)] #! (1)
    
    for query in queries:
        x1, y1, x2, y2 = query
        min_value = float('inf') # 최솟값
        prev_value = matrix[x1-1][y1-1] # 처음값
        # 윗줄 - 임시저장 후 적용 + 시계방향순으로 진행 #! (2) x,y를 좌표로 사용
        for y in range(y1, y2): 
            current_value = matrix[x1-1][y]
            matrix[x1-1][y] = prev_value
            prev_value = current_value
            min_value = min(min_value, prev_value)

        # 오른쪽
        for x in range(x1, x2):
            current_value = matrix[x][y2-1]
            matrix[x][y2-1] = prev_value
            prev_value = current_value
            min_value = min(min_value, prev_value)

        # 아랫줄
        for y in range(y2-2, y1-2, -1):
            current_value = matrix[x2-1][y]
            matrix[x2-1][y] = prev_value
            prev_value = current_value
            min_value = min(min_value, prev_value)

        # 왼쪽
        for x in range(x2-2, x1-2, -1):
            current_value = matrix[x][y1-1]
            matrix[x][y1-1] = prev_value
            prev_value = current_value
            min_value = min(min_value, prev_value)

        answer.append(min_value) #! (3)
    return answer
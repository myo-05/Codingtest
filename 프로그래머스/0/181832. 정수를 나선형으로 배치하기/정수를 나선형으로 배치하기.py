def solution(n):
    answer = [[0]*n for _ in range(n)]
    x,y = 0,0 # 시작점
    num = 1 # 시작값
    directions = [(0,1), (1,0), (0,-1), (-1,0)] # 방향리스트 - 우하좌상
    dir_index = 0 # 방향인덱스
    while num <= n**2:
        answer[x][y] = num # 값 저장
        num += 1 # 값 증가
        
        next_x = x+directions[dir_index][0] # 다음x좌표
        next_y = y+directions[dir_index][1] # 다음y좌표
        
        if 0 <= next_x < n and 0 <= next_y < n and answer[next_x][next_y] == 0: # 다음좌표가 유효하다면
            x,y = next_x,next_y # 다음좌표로 이동
        else: # 아니라면
            dir_index = (dir_index+1)%4 # 다음방향
            x += directions[dir_index][0] # 다음x좌표
            y += directions[dir_index][1] # 다음y좌표
    return answer
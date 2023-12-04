def solution(board, h, w):
    n = len(board) # 보드의 길이
    count = 0 # 같은 색의 개수
    
    # 상하좌우 dh,dw =(-1,0) (1,0) (0,-1) (0,1)
    dh = [-1,1,0,0]
    dw = [0,0,-1,1]
    
    for i in range(4):
        check_h = h + dh[i]
        check_w = w + dw[i]
        if 0 <= check_h < n and 0 <= check_w < n : # 보드의 범위를 벗어나지 않는다면 
            if board[check_h][check_w] == board[h][w]: # 색 비교
                count += 1 # 동일 색상 갯수 추가
    return count
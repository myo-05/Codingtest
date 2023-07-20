def move(current,op,n):
    vector = {'N':(-n,0),'S':(n,0),'W':(0,-n),'E':(0,n),}
    if op in vector:
        return [current[0]+vector[op][0],current[1]+vector[op][1]]

def solution(park, routes):
    H,W = len(park), len(park[0])

    for i,h in enumerate(park):
        for j,w in enumerate(h):
            if w == "S":
                current = [i,j] #시작위치

    for route in routes:
        op,n = route[0],int(route[2]) # 방위와 이동거리 정의
        moved = move(current,op,n) # 명령 수행 시 이동 좌표
        if 0<= moved[0] < H and 0<= moved[1] < W: # 좌표범위 내인지 판별
            # 장애물과 충돌 판별
            for i in range(n):
                i += 1
                moving = move(current,op,i) # 한칸씩 이동
                h,w = moving[0],moving[1]
                if park[h][w] == "X":
                    break
            else: # 장애물이 없다면
                current = moved # 현재위치로 저장
    return current
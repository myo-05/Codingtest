def solution(n, w, num):
    storages = [[0]*w for _ in range((n//w+1))]
    # 택배 상자 적재
    i = 1
    while i <= n:
        floor = i//w
        if floor%2:
            for j in range(w-1,-1,-1):
                storages[floor][j] = i
                i += 1  
                if i > n:
                    break
        else:
            for j in range(w):
                storages[floor][j] = i
                i += 1
                if i > n:
                    break
    # 택배 위치 찾기
    for idx,storage in enumerate(storages):
        try:
            print(idx,storage.index(num))
            target = idx,storage.index(num)
            break
        except:
            continue
    box = 1
    # 꺼내야 하는 상자 수
    for i in range(n//w,target[0],-1):
        if storages[i][target[1]]:
            box += 1
    return box         
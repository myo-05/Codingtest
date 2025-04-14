def solution(mats, park):
    for mat in sorted(mats,reverse=True):
        for i in range(len(park)-mat+1):
            for j in range(len(park[0])-mat+1):
                if park[i][j] != "-1":
                    continue
                for x in range(mat):
                    for y in range(mat):
                        if park[i+x][j+y] != "-1":
                            break
                    else:
                        continue
                    break
                else:
                    return mat
    return -1
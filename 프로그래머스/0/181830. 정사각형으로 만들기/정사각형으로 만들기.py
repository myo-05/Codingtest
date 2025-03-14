def solution(arr):
    row,col = len(arr),len(arr[0])
    if row==col:
        return arr
    elif row>col:
        for a in arr:
            a += [0]*(row-col)
    else:
        for _ in range(col-row):
            arr.append([0]*col)
    return arr
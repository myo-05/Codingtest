def solution(arr):
    if 2 not in arr:
        return [-1]
    start,end = -1,-1
    for i,n in enumerate(arr):
        if n == 2 and start == -1 :
            start = i
            end = i
        elif n == 2 :
            end = i
    answer = arr[start:end+1]
    return answer
def solution(arr, queries):
    answer = []
    for query in queries:
        s,e,k = query
        tmp = []
        for i in range(s,e+1):
            if arr[i] > k:
                tmp.append(arr[i])
        try:
            answer.append(min(tmp))
        except:
            answer.append(-1)
    return answer
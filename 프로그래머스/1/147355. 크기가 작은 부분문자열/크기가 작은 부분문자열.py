def solution(t, p):
    answer = 0
    s,l = len(t),len(p)
    for i in range(s-l+1):
        print(t[i:i+l])
        if t[i:i+l] <= p:
            answer += 1
    return answer
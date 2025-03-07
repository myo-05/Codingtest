def solution(intStrs, k, s, l):
    answer = []
    for str in intStrs:
        target = int(str[s:s+l])
        if target > k:
            answer.append(target)
    return answer
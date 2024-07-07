def solution(s):
    answer = []
    for n,i in enumerate(s):
        tmp = s[:n][::-1]
        count = 1
        if i not in tmp:
            answer.append(-1)
            continue
        for j in tmp:
            if i == j:
                answer.append(count)
                break
            count += 1
    return answer
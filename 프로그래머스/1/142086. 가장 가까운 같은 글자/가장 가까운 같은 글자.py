def solution(s):
    answer = []
    for n,i in enumerate(s):
        tmp = s[:n][::-1]
        count = 1
        for j in tmp:
            if i == j:
                answer.append(count)
                break
            else: count += 1
        else: answer.append(-1)
    return answer
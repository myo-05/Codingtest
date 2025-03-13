def solution(strArr):
    answer = dict.fromkeys(range(1,31),0)
    for s in strArr:
        answer[len(s)] += 1
    return max(answer.values())
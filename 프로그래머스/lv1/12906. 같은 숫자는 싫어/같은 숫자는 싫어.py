def solution(arr):
    answer = []
    for i in arr:
        if answer == []:
            answer.append(i)
        if i == answer[-1]:
            continue
        else:
            answer.append(i)
    return answer
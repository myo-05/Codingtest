def solution(numlist, n):
    answer = []
    for num in numlist:
        answer.append([num,abs(n - num)])
    answer.sort(key=lambda x: x[0], reverse=True)
    answer.sort(key=lambda x: x[1])
    return [i[0] for i in answer]
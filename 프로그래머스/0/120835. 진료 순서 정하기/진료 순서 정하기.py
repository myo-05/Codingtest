def solution(emergency):
    answer = [0]*len(emergency)
    for i,e in enumerate(sorted(emergency,reverse=True),1):
        answer[emergency.index(e)] = i
    return answer
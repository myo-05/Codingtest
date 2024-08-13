def solution(elements):
    answer = 0
    l = len(elements) # 원형수열의 길이
    elements = elements*2
    tmp = [] # 연속 부분 수열 합 저장
    for i in range(1,l+1):
        for j in range(l):
            tmp.append(sum(elements[j:j+i]))
    return len(set(tmp)) # 중복을 제외한 가짓수
def solution(k, score):
    '''
    날마다 ranker=[] 갱신
        min(ranker)와 새 score 요소 비교 후 추가 or continue
    날마다 min(ranker) answer=[]에 추가
    min(ranker) 대신 sort 활용
    '''
    ranker = []
    answer = []
    for s in score:
        if len(ranker) != k: # 명예의 전당이 모두 차지 않았다면
            ranker.append(s)
        else: # 명예의 전당이 모두 찼다면 점수비교
            if ranker[-1] < s:
                ranker.pop()
                ranker.append(s)
        ranker.sort(reverse=True) # 순위정렬
        answer.append(ranker[-1]) # 최하위 점수 저장
    return answer
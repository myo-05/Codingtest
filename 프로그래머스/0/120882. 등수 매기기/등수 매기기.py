def solution(score):
    answer = []
    
    # 평균 구하기
    mean = []
    for s in score:
        mean.append(sum(s)/len(s))
    # 평균 기준으로 등수 새기기
    rank = sorted(mean,reverse=True)
    # 동점은 공동 순위로 하고, 공동으로 인해 부재되는 등수 고려하기
    for m in mean:
        answer.append(rank.index(m)+1)
    return answer
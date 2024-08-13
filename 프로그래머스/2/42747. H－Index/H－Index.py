'''
논문 n편 중, h번 이상 인용된 논문(a)이 h편 이상이고 
나머지 논문(b=n-a)이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.
'''
def solution(citations):
    l = len(citations) # 논문개수
    for i in range(l,-1,-1): # 논문개수 내림차 순회
        citations.append(i) # 인덱스용 추가
        citations.sort() # 인용수 오름차순 정렬
        enough = l - citations.index(i) # i번 이상 인용된 논문 개수
        if enough >= i: # 처음으로 만족할 경우가 최댓값, 즉 H-Index
            return i
        citations.remove(i) # 인덱스용 제거
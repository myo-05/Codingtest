from itertools import combinations as cb
def solution(numbers):
    answer = []
    for i in cb(numbers,2): # combinations로 조합 생성 / 서로 다른 인덱스
        print(i)
        answer.append(sum(i)) # 순회하면서 합을 추가
    return sorted(set(answer)) # set으로 중복 제거 및 오름차순 정렬
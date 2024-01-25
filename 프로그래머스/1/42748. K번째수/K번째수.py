def solution(array, commands):
    # 1) i~j 잘라내고 '정렬'하여 list저장
    # 2) list에서 k번째 수 추출
    # 3) 1~2 과정을 commands를 순회하며 수행하여 answer에 저장
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(sorted(array[i-1:j])[k-1]) # 1,2,3
    return answer
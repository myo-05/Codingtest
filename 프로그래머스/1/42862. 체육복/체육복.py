'''
여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다.
    이때 이 학생은 체육복을 하나만 도난당했다고 가정하며,
    남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
'''
def solution(n, lost, reserve):
    answer = n - len(lost) # 수업을 들을 수 있는 학생수
    for i in lost[:]:
        if i in reserve: # 자신의 옷이있다면
            reserve.remove(i) # 여벌에서 제거
            answer += 1 # 수업가능학생 추가
            lost.remove(i) # 도난자에서 제거
    for i in sorted(lost): # 번호순 정렬
        if i-1 in reserve: # 앞번호 여벌이 있다면
            reserve.remove(i-1) # 여벌에서 제거
        elif i+1 in reserve: # 뒷번호 여벌이 있다면
            reserve.remove(i+1) # 여벌에서 제거
        else:
            continue # 없다면 다음
        answer += 1 # 수업가능학생 추가
    return answer
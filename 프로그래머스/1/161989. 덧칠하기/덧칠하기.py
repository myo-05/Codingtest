'''
n 벽의 총 길이 int
m 롤러의 길이 int
section 칠해야하는 벽의 위치 list
'''
def solution(n, m, section):
    answer = tmp = 0
    for i in section:
        if i <= tmp : continue # 이미 칠한 벽이라면 패스
        if n <= tmp : break # 마지막까지 칠했다면 중단
        tmp = i + m - 1 # 한번에 칠해지는 범위 업데이트
        answer += 1 # 칠한 횟수 추가
    return answer
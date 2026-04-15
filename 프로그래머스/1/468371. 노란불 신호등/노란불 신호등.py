"""
1. 항상 초록불 → 노란불 → 빨간불 순서로 반복
2. 모든 신호등이 모두 노란불이 되면 정전
모든 신호등이 노란불이 되는 가장 빠른 시각(초)을 return , 없을 경우 -1
"""
# 시간만큼 문자열로 표현해서 교차지점 찾기 + 시간 제약 활용 판별
def solution(signals):
    trans_signal = []
    temp = ''
    # 문자열로 변환
    for signal in signals: 
        G,Y,R = signal
        temp += '0'*G + '1'*Y + '0'*R
        trans_signal.append(temp)
        temp = ''
    # 교차지점 찾기
    first = trans_signal[0]
    for i in range(len(trans_signal)-1):
        second = trans_signal[i+1]
        f = len(first)
        s = len(second)
        print(f,s)
        cross = ''
        for j in range(f*s): # 최대 시간 산정
            cross += str(int(first[j%f]=='1' and second[j%s]=='1'))
        first = cross # 교차 결과로 대체
    
    black_out_time = cross.find('1') + 1 # index를 time으로 변환
    
    return black_out_time if black_out_time else -1

def solution(s):
    binary_count = 0
    zero_count = 0
    while s != "1": # s가 "1"이 될 때까지 반복
        binary_count += 1 # 이진변환 횟수 카운트
        l = len(s.replace("0","")) # 모든 0 제거 후 길이 
        zero_count += len(s)-l # 제거된 0의 개수 카운트
        s = bin(l)[2:] # 2진법 변환
    return [binary_count,zero_count]
def solution(s):
    x = s[0] # 문자열의 첫 글자
    first, other, answer = 0, 0, 0
    for i,a in enumerate(s):
        if a == x:
            first += 1
        else:
            other += 1
        if first == other or len(s)==i+1: # 분리조건 달성 시
            answer += 1 # 문자열 갯수 추가
            first, other = 0, 0 # 리셋
            try :
                x = s[i+1] # 문자열의 첫 글자 업데이트
            except:
                break
    return answer
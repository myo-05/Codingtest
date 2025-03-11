# x를 기준으로 문자열 잘라내어 리스트에 담기
# 빈 문자열 제외
# 사전순으로 정렬하여 리턴

def solution(myString):
    answer = []
    for s in sorted(myString.strip('x').split('x')):
        if s  == '':
            continue
        else:
            answer.append(s)
    return answer
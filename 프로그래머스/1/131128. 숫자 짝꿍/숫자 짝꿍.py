'''
input: 정수 문자열 X Y 
return: 짝꿍 정수 문자열
- X Y 각각의 숫자 개수 저장
- 숫자와 개수를 비교하여 공통수 뽑기
- 짝궁 생성
- 짝궁이 0 이라면 0
- 짝궁이 없다면 -1 반환
'''
def solution(X, Y):
    share_num = {} # 공통수 저장
    X_num = {}
    Y_num = {}
    for x in X:
        X_num[x] = X_num.get(x, 0) + 1 # X 숫자 개수 저장
    for y in Y:
        Y_num[y] = Y_num.get(y, 0) + 1 # Y 숫자 개수 저장
    for k,v in X_num.items():
        try:
            share_num[k] = min(Y_num[k],v) # 공통수 개수 저장
        except:
            continue
    if share_num == {}: 
        return "-1" # 공통수가 없다면 -1
    elif len(share_num) == 1 and share_num.get('0',False): 
        return '0' # 공통수가 0만 있다면 0
    answer = ''
    for i in sorted(share_num.keys(),reverse=True):
        answer += i*share_num[i]
    return answer
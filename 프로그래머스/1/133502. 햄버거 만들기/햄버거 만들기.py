def solution(ingredient):
    answer = 0 # 완성된 햄거버 개수
    stack = []
    for i in ingredient:
        stack.append(i) # stack에 저장
        if stack[-1:-5:-1] == [1,3,2,1]: # 햄버거가 완성되면
            del stack[-1:-5:-1] # 재료제거
            answer += 1 # 완성된 햄거버 개수 추가
    return answer
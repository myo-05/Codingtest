def solution(prices):
    n = len(prices)
    answer = [0]*n
    stack = []
    
    for idx,price in enumerate(prices):
        while stack and stack[-1][1] > price: # stack이 비어있지 않고, 가격이 떨어지면
            answer[stack[-1][0]] = idx-stack[-1][0] # 시간계산 후 저장
            stack.pop() # stack에서 제거
        stack.append([idx,price]) # stack에 추가
    
    for idx,price in stack: # stack에 쌓인 끝까지 떨어지지 않은 값
        answer[idx] = n-1-idx # 시간계산 후 저장
        
    return answer
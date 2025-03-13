def solution(arr, n):
    answer = []
    odd = 0 if len(arr)%2 else 1
    even = 1 if len(arr)%2 else 0
        
    for i,a in enumerate(arr):
        if i%2 == 0:
            answer.append(a+n*even)
        else:
            answer.append(a+n*odd)
            
    return answer
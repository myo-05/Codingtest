def solution(arr):
    def function(arr,x):
        result = arr
        for _ in range(x):
            answer = []
            for i in result:
                if i >= 50 and i%2 == 0:
                    i=i//2
                elif i < 50 and i%2 != 0:
                    i = i*2+1
                answer.append(i)
            result = answer
        return result
    
    x = 0
    while function(arr,x) != function(arr,x+1):
        x += 1
    return x
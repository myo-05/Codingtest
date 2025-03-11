def solution(num_list):
    def func_count(x):
        count = 0
        while x != 1:
            count += 1
            if x%2 == 0:
                x = x//2
            else:
                x = (x-1)//2
        return count
    
    answer = 0
    for num in num_list:
        answer += func_count(num)
    return answer
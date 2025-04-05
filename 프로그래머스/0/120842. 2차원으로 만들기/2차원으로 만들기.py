def solution(num_list, n):
    answer = []
    tmp = []
    for i,num in enumerate(num_list,1):
        tmp.append(num)
        if i%n == 0:
            answer.append(tmp)
            tmp = []
    return answer
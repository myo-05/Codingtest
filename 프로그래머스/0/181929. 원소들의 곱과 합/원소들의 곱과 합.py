def solution(num_list):
    # 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0
    num_sum = 0
    num_times = 1 
    for num in num_list:
        num_sum += num
        num_times *= num
    return int(num_times < num_sum**2)
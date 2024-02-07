def solution(num_list):
    last_num = num_list[-1]
    before_num = num_list[-2]
    
    if last_num > before_num : # 마지막 원소가 그전 원소보다 크면 마지막 원소에서 그전 원소를 뺀 값
        num_list.append(last_num-before_num)
    else: # 마지막 원소가 그전 원소보다 크지 않다면 마지막 원소를 두 배한 값을 추가
        num_list.append(last_num*2)
    return num_list
def solution(a, b, c, d):
    dice_list = [a,b,c,d]
    unique_num = list(set(dice_list)) # 중복제외 리스트
    num_count = len(unique_num) # 중복제거 요소갯수
    if num_count == 1:
        return 1111*a
    if num_count == 2:
        if dice_list.count(unique_num[0]) != 2:
            if dice_list.count(unique_num[0]) == 3:
                p,q = unique_num[0],unique_num[1]
            else:
                q,p = unique_num[0],unique_num[1]
            return (10*p + q)**2
        else:
            p , q = unique_num[0],unique_num[1]
            return (p + q) * abs(p - q)
    if num_count == 3:
        for num in unique_num:
            if dice_list.count(num) == 2 :
                unique_num.remove(num)
                break
        q,r = unique_num[0],unique_num[1] 
        return q * r
    return min(dice_list)
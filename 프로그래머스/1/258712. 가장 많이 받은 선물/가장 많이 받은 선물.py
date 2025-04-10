def solution(friends, gifts):
    # 다음 달 선물 받을 수
    next_month_gift = dict.fromkeys(friends,0) 
    # 선물지수
    gifts_point = dict.fromkeys(friends,0)
    # 선물받은 대상
    receive_from = {friend: dict.fromkeys(friends,0) for friend in friends}
    for gift in gifts:
        From,To = gift.split(' ')
        gifts_point[From] += 1
        gifts_point[To] -= 1
        receive_from[To][From] += 1
    
    # 두 사람 선물기록 비교
    for i in range(len(friends)):
        for j in range(i+1,len(friends)):
            # i가 더 줬을 경우
            if receive_from[friends[i]][friends[j]] < receive_from[friends[j]][friends[i]]:
                next_month_gift[friends[i]] += 1
            # j가 더 줬을 경우    
            elif receive_from[friends[i]][friends[j]] > receive_from[friends[j]][friends[i]]:
                next_month_gift[friends[j]] += 1
            # 주고받은 선물이 없거나 같을 경우 - 선물지수 비교
            else:
                if gifts_point[friends[i]] > gifts_point[friends[j]]:
                    next_month_gift[friends[i]] += 1
                elif gifts_point[friends[i]] < gifts_point[friends[j]]:
                    next_month_gift[friends[j]] += 1                    
    return max(next_month_gift.values())
def solution(lottos, win_nums):
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6} # 맞춘 개수 별 순위
    zero_count, count = sum(1 for x in lottos if x == 0 ), sum(1 for num in win_nums if num in lottos) # 미확인 번호 개수, 일치 번호 개수
    high_rank, low_rank = rank[count+zero_count], rank[count] # 미확인이 모두 일치할 경우, 미확인이 모두 불일치할 경우 순위
    return [high_rank, low_rank]
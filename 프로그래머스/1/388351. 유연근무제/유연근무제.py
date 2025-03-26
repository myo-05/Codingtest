def solution(schedules, timelogs, startday):
    answer = 0 # 상품수령인
    for schedule,timelog in zip(schedules,timelogs):
        days = [i%7 for i in range(startday,startday+7)] # 요일
        save = ( schedule//100 + (schedule%100+10)//60 )*100 + (schedule%100+10)%60 # 인정시간
        # 지각체크
        for time,day in zip(timelog,days):
            if day in (6,0) : # 주말이면 패스
                continue
            if save < time: # 지각했다면
                break # 탈락
        else: # 지각하지 않았다면
            answer += 1 # 상품수령인 추가
    return answer

def solution(progresses, speeds):
    answer = []
    duty_day = []

    for i,j in zip(progresses,speeds): # 작업에 소요되는 일자 계산
        day = (100-i)//j+1 if (100-i)%j else (100-i)//j
        duty_day.append(day)
    while duty_day:
        deploy = duty_day[0]
        count = 0
        for day in duty_day[::]:
            if deploy >= day:
                count += 1
                a = duty_day.pop(0)
            else:
                break
        answer.append(count)
    return answer
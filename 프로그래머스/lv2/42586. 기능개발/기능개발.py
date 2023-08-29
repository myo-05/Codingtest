def solution(progresses, speeds):
    answer = []
    duty_day = []

    for i,j in zip(progresses,speeds):
        if (100-i)%j != 0:
            duty_day.append((100-i)//j+1)
        else:
            duty_day.append((100-i)//j)
    duty_day.reverse()
    
    while duty_day:
        deploy = duty_day[-1]
        count = 0
        for day in duty_day[::-1]:
            if deploy >= day:
                count += 1
                duty_day.pop()
            else:
                break
        answer.append(count)
    return answer
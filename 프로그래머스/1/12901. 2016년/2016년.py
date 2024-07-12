def solution(a, b):
    week_list = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    days_dict = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    first_day = 'FRI'
    
    date_diff = b - 1 + sum(days_dict[m] for m in range(1,a))
    day_index = (week_list.index(first_day) + date_diff%7)%7
    answer = week_list[day_index]
    return answer
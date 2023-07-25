def solution(dartResult):
    saved = ''
    save_list = []
    for x in dartResult:
        if x in "SDT":
            save_list.append(int(saved)**("SDT".index(x)+1))
            saved = ''
            continue
        elif x in "*#":
            if x == "*": # 스타상(*)
                if len(save_list) == 1:
                    a = save_list.pop()*2
                    save_list.append(a)
                else:
                    a = save_list.pop()*2
                    b = save_list.pop()*2
                    save_list.append(b)
                    save_list.append(a)
            elif x == "#": # 아차상(#)
                save_list.append(save_list.pop()*(-1))
            continue
        saved += x
    return sum(save_list)
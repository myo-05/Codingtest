def solution(id_list, report, k):

    note={}
    banner=[]
    for i in set(report):
        a=i.split(" ") 
        try:
            note[a[0]] += [a[1]]
        except:
            note[a[0]] = [a[1]]
        banner.append(a[1])
    
    user_dict={} #신고당한 횟수를 저장할 딕셔너리
    for i in id_list:
        user_dict[i]=0
    for ban in banner:
        user_dict[ban] +=1 #신고당한 횟수 카운트
    
    pause=[] # 정지대상을 저장할 리스트
    for i in id_list:
        if user_dict[i] >= k:
            pause.append(i)
        user_dict[i]=0 # 처리결과메일 개수를 저장하기 위해 리셋
        
    for key,value in note.items(): # 신고자: 피신고자 명단
        for i in pause: 
            if i in value: # 정지대상이 피신고자에 있다면
                user_dict[key] +=1 # 처리결과메일 개수 추가
    
    answer = list(user_dict.values()) # 처리결과메일 수를 저장한 리스트
    return answer
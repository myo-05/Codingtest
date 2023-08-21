def solution(today, terms, privacies):
    #오늘 날짜를 년,월,일 로 받은 후 → 일단위로 변환하여 저장
    [year,month,day] = today.split(".")
    today = sum([int(year)*12*28,int(month)*28,int(day)])
    #약관종류와 유효기간이 쌍값 → dict저장 + 유효기간은 일단위로
    terms_dict = {}
    for term in terms:
        typ,exp = term.split(" ")
        terms_dict[typ] = int(exp)*28
    #파기목록 선언
    expired_list = []
    #개인정보 수집일자와 약관종류 분리
    for i,privacie in enumerate(privacies,1):
        day,typ = privacie.split(" ")
        #수집일자 일단위로 변환
        [year,month,day] = day.split(".")
        day = sum([int(year)*12*28,int(month)*28,int(day)])
        #약관종류 별 유효성 판별하여 파기목록에 추가
        for typ_,exp in terms_dict.items():
            if typ == typ_:
                if (today-day) >= exp:
                    expired_list.append(i)  
    return expired_list
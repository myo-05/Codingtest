def solution(s):
    '''
    1) i개씩 임시누적저장하며 압축가능유무 판별 - 슬라이싱 사용
    2) 압축후 최종 문자열의 길이를 result_list에 저장
    3) 1 <= i <= len(s) 반복문
    4) min(result_list) 결과 return 
    '''
    result_list=[]
    for i in range(1, len(s)+1): # i자씩 끊기!
        cut_str = ''
        cnt = 1 # 중복카운트
        cut_before = s[:i] # 비교 문자열(1)

        for j in range(i, len(s)+i, i): # i부터 끝까지 i단위로 나누어 탐색
            cut_next = s[j:i+j] # 비교 문자열(2)
            if cut_before==cut_next: # 앞 뒤가 같다면 
                cnt += 1 # 카운트추가
                
            else: # 앞 뒤가 다르다면
                if cnt != 1: # 중복 카운트가 있었다면
                    cut_str = cut_str + str(cnt)+cut_before # 글자 만들기
                else:
                    cut_str = cut_str + cut_before
        
                cut_before = s[j:j+i] # 비교 문자열(1) 초기화
                cnt = 1 # 중복카운트 초기화
        result_list.append(len(cut_str)) # 최종 문자열의 길이 리스트에 저장
        
    return min(result_list) # 가장 작은 수
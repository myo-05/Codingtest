# 단어는 공백으로 구분되며, 알파벳 소문자와 숫자로만 구성된 연속된 문자열
# 중요단어 - 아래 모두 만족
    # 1. 스포 방지 단어여야 합니다. -> 스포일러 구간에 들어있어야 한다.
    # 2. 메시지의 스포 방지 구간이 아닌 구간(= 어떤 스포 방지 구간에도 속하지 않는 모든 구간: 각 구간의 앞·사이·뒤 포함)에 등장한 적이 없어야 합니다. -> 반드시 스포 구간에만 있어야한다.
    # 3. 이전에 공개된 스포 방지 단어와 중복되지 않아야 합니다. -> 중복은 처음 하나만 인정
    # 4. 여러 단어가 동시에 공개된 경우, 왼쪽부터 순서대로 하나씩 중요한 단어인지 판단합니다. -> 순차적 탐색

def solution(message, spoiler_ranges):
    answer = 0 # 중요단어 수
    message_list = message.split() # 전체 단어
    spoiler_message = [] # 스포 방지 단어
    non_spoiler_message = [] # 일반 단어
    m_start = 0
    m_word = "" # 단어
    for i,m in enumerate(message):
        m_word += m
        m_word = m_word.strip() # 공백제거
        if m == " " or i == len(message)-1: # 단어단위 판별
            # 시작점,끝점
            m_start = m_start
            m_end = i-1
            # 단어중 스포인 단어 판별
            for spoiler in spoiler_ranges:
                s_start,s_end = spoiler
                if m_start <= s_end and s_start <= m_end:
                    spoiler_message.append(m_word) # 1. 스포 방지 단어
                    break
            else:
                non_spoiler_message.append(m_word) # 2. 일반 단어
            # 초기화
            m_start = i+1 # 시작점 초기화
            m_word = "" # 단어 초기화
    spoiler_message = set(spoiler_message) # 3&4.중복 스포는 처음 하나만 인정

    # 중요단어 판별
    for spoiler in spoiler_message: # 1. 스포 방지 단어에 포함
        if spoiler not in non_spoiler_message: # 2. 일반단어에 미포함해야한다.
            answer += 1
    return answer
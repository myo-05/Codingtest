def solution(n):
    word = '수박'
    word_n = n//len(word) # 온전한 단어 갯수
    parts_n = n%len(word) # 부분 단어 수
    
    return word*word_n + word[:parts_n]
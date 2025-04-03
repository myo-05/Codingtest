def solution(age):
    mode = 'abcdefghij'
    return ''.join(mode[int(n)] for n in str(age))
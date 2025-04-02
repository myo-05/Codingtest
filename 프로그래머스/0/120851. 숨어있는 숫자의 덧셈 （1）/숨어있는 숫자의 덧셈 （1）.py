def solution(my_string):
    return sum(int(s) for s in my_string if not s.isalpha())
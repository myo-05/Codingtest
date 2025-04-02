def solution(num_list):
    odd = sum(n%2 for n in num_list)
    even = len(num_list)-odd
    return [even,odd]
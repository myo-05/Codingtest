def prime_num(num):
    if num <= 1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i == 0: # 나누어 떨어지면 소수가 아니다
            return False
    return True

from itertools import permutations as perm
def solution(numbers):
    num_list = [] # 종이의 각 번호를 담을 배열
    for num in numbers:
        num_list.append(int(num))

    count = 0
    num_pmt = []
    for l in range(1,len(num_list)+1):
        for s in perm(num_list,l):
            number = ''
            for r in s:
                number += str(r)
            num_pmt.append(int(number))
    for num in set(num_pmt):
        if prime_num(int(num)):
            count += 1
    return count
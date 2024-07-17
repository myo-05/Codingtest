import itertools

def prime_number(number):
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

def solution(nums):
    count = 0
    iterator = itertools.combinations(nums,3)
    for comb in iterator:
        sum_ = sum(comb)
        if prime_number(sum_) :
            count += 1
    return count
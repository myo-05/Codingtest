def solution(n):
    answer = 0
    def divisor_count(num):
        count = 0
        for i in range(1,int(num**0.5)+1):
            if num%i == 0:
                count += 2
            if num**0.5 == i:
                count -= 1
        return count
    return sum(divisor_count(i) >= 3 for i in range(1,n+1))
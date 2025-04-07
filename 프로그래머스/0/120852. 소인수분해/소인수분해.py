def solution(n):
    prime_factor_unique = set()
    divisor = 2 
    while divisor <= n**0.5:
        while n%divisor == 0:
            prime_factor_unique.add(divisor)
            n //= divisor
        divisor += 1
    if n>1:
        prime_factor_unique.add(n)          
    return sorted(list(prime_factor_unique))
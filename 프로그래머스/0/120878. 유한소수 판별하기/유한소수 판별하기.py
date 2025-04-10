def solution(a, b):
    def irreducible_fraction(a,b):
        for i in range(a,0,-1):
            if a%i == 0 and b%i == 0:
                b //= i
                a //= i
                return a,b
    
    def prime_factor_unique(num:int) -> set:
        factor = set()
        x = 2
        while x<=num**0.5:
            while num%x == 0:
                factor.add(x)
                num //= x
            x += 1
        if num>1:
            factor.add(num)
        return factor
    
    a,b = irreducible_fraction(a,b)
    
    return 2 - int(prime_factor_unique(b).issubset({2,5}))
def solution(numer1, denom1, numer2, denom2):
    n1,d1,n2,d2 = numer1, denom1, numer2, denom2
    n = n1*d2 + n2*d1
    d = d1*d2
    
    for i in range(min(n,d),0,-1):
        if d%i == 0 and n%i == 0:
            n,d = n/i, d/i
    return [n,d]
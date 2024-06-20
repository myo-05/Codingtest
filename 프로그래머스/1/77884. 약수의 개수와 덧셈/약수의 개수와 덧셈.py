def divisor_count(x):
    divisor = []
    for i in range(1,int(x**0.5)+1):
        if x%i == 0 :
            divisor.append(i)
            divisor.append(x//i)
    return len(set(divisor))

def solution(left, right):
    return sum( -n if divisor_count(n)%2 else n for n in range(left,right+1))

def solution(n,a,b):
    rounds = 0
    while True:
        rounds += 1
        a = int(a/2+0.5)
        b = int(b/2+0.5)
        if a == b:
            return rounds        

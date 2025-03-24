def solution(n):
    MOD = 1234567
    
    dp = [0]*(n+1)
    
    # 초기값
    dp[0] = 1
    if n >= 1:
        dp[1] = 1
    
    # 점화식
    for i in range(2,n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % MOD
        
    return dp[n]
def solution(ineq, eq, n, m):
    answer = [n>=m,n>m] if ineq == ">" else [n<=m,n<m]
    return int(answer[0] if eq == "=" else answer[1])
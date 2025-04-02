def solution(n, k):
    food_price = {'skewer':12000,'drink':2000}
    k -= n//10
    total = food_price['skewer']*n + food_price['drink']*k
    return total
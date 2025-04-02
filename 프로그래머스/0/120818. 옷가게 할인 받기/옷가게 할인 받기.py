def solution(price):
    answer = price
    price_discount = {'100000':0.05, '300000':0.1, '500000':0.2}
    for p,d in price_discount.items():
        if price >= int(p):
            answer = price*(1-d)
    return answer//1
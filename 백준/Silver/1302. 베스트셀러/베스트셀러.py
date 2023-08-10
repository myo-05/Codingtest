import sys
input = sys.stdin.readline
n = int(input())

seller = {}
bestseller = []
for _ in range(n):
    book = input()
    try:
        seller[book] += 1
    except:
        seller[book] = 1
for k,v in seller.items():
    if v == max(seller.values()): # 베스트셀러일 경우
        bestseller.append(k)
bestseller.sort() # 오름차순
print(bestseller[0]) # 베스트셀러 출력
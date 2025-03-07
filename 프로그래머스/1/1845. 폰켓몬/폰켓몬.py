'''
최대한 많은 종류의 폰켓몬
'''
def solution(nums):
    return min(len(set(nums)),len(nums)/2)

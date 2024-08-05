def solution(brown, yellow):
    '''
    brown+yellow=(a+2)*(b+2)
    yellow=a*b
    '''
    area = brown+yellow
    for a in range(1,int(yellow**0.5)+1):
        if yellow % a == 0:
            b = yellow//a
            if (a+2)*(b+2) == area :
                return [(b+2),(a+2)]
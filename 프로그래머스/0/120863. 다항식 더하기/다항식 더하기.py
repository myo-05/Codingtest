def solution(polynomial):
    x,const = 0,0
    for p in polynomial.split(' + '):
        print(p)
        if 'x' in p:
            x += 1 if 'x' == p else int(p.replace('x',''))
        else:
            const += int(p)
            
    answer = []
    if x == 1:
        answer.append('x')
    elif x > 1:
        answer.append(str(x)+'x')
    if const != 0:
        answer.append(str(const))
        
    return ' + '.join(answer)
def solution(wallpaper):
    x =[]
    y = []
    for i,v in enumerate(wallpaper):
        if '#' in v:
            for j,w in enumerate(v):
                if w == '#':
                    x.append(i)
                    y.append(j)
    start= [min(x),min(y)]
    end= [max(x)+1,max(y)+1]
    return start + end
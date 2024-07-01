def solution(sizes):
    w,h = 0,0
    for x,y in sizes:
        x,y = max(x,y),min(x,y)
        w,h = max(w,x),max(h,y)
    return w*h
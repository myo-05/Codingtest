def solution(bandage, health, attacks):
    max_health = health
    t,x,y = bandage
    keep = 0
    time = 0
    attacks.sort(reverse=True)
    while attacks:
        time += 1
        if time == attacks[-1][0]:
            health -= attacks.pop()[1]
            keep = 0
        else:
            keep += 1
            if keep == t:
                health += y
                keep = 0
            health += x
        health = min(health,max_health)
        if health <= 0:
            return -1
    return health
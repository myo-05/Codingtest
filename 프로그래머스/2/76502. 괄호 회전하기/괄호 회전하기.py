def solution(s):
    answer = 0
    for _ in s:
        s=s[1:]+s[:1]
        a=s
        while "()" in a or "[]" in a or "{}" in a:
            a=a.replace("()","").replace("[]","").replace("{}","")
            if a == "":
                answer += 1
                break
    return answer
def solution(survey, choices):
    survey_count={"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    for i,s in enumerate(survey):
        if (choices[i]-4) >= 0:
            survey_count[s[1]] += (choices[i]-4)
        else:
            survey_count[s[0]] += abs(choices[i]-4)
    answer = ''
    answer += "R" if survey_count["R"]>=survey_count["T"] else "T"
    answer += "C" if survey_count["C"]>=survey_count["F"] else "F"
    answer += "J" if survey_count["J"]>=survey_count["M"] else "M"
    answer += "A" if survey_count["A"]>=survey_count["N"] else "N"
    return answer
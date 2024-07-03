def solution(s):
    num_list= ["zero","one","two","three","four","five","six","seven","eight","nine"]
    
    for i,num in enumerate(num_list):
        if num in s:
            s = s.replace(num,str(i))
    return int(s)
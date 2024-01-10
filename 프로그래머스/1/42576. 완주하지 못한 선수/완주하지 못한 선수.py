from collections import Counter

def solution(participant, completion):
    
    p_count = Counter(participant)
    c_count=Counter(completion)
    answer= list((p_count-c_count).keys())[0]
    return answer
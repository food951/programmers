def solution(s):
    try :
        num= int(s)
        if (len(s)==4 or len(s) ==6):
            answer = True
        else :
            answer = False    
    
        return answer
    except ValueError:
        return False
def solution(s):
    nump=0
    numy=0
    for i in range(len(s)):
        if s[i]=="p" or s[i]=="P":
            nump+=1;
        elif s[i]=="y" or s[i]=="Y":
            numy+=1
    return nump ==numy  
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
        
    
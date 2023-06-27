def solution(s):
    
    list1= list(s)
    list1[0]=list1[0].upper()
    for i in range(1,len(s)):
        if list1[i-1]==" ":
            list1[i]=list1[i].upper()
        else :
            list1[i]=list1[i].lower()
    answer="".join(list1)
    return answer
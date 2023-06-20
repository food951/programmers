def solution(n):
    answer = 0;
    n3=''
    if n==0:
        answer = 0;
    
    while n>0:
        n,n_3 =divmod(n,3)
        n3= str(n_3)+n3
    list3= list(n3)
    list3.reverse()
    rev = "".join(list3)
    answer = int(rev,3)
    return answer
def solution(a, b, n):
    count= 0
    while True:
        count += (n//a)*b
        n =(n//a)*b + n-((n//a)*a)
        if n<a:
            break
    return count
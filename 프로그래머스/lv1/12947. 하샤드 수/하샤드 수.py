def solution(x):
    summ=0
    str1=str(x)
    for i in range(len(str1)):
        summ += int(str1[i])
    
    return x%summ==0
   
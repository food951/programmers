from collections import Counter
def solution(nums):
    num1=len(nums)
    n_count=Counter(nums)
    num2=len(list(n_count.keys()))
    return min(num1/2,num2)  
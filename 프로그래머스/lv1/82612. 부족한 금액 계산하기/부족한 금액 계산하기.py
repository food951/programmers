def solution(price, money, count):
    cost = price * (count * (count + 1)) // 2
    if cost < money:
        return 0
    else:
        return cost - money
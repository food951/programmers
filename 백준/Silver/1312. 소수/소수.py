a, b, c = map(int, input().split())
d = (a * 10**c) // b % 10
print(int(d))
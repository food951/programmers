a, b = map(int, input().split())
score1 = (a + b) // 2
score2 = (a - b) // 2

if (a + b) % 2 == 0 and (a >= b):
    print(score1, score2)
else:
    print(-1)
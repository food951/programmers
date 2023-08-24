a,b= input().split()
c,d= input().split()
a,b,c,d=int(a),int(b),int(c),int(d)
def find_gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

gcd_numer = find_gcd(a * d + c * b, b * d)
gcd_denom = b * d

# 최대공약수로 분수 간소화
num = (a * d + c * b) // gcd_numer
den = gcd_denom // gcd_numer
print (num,den)
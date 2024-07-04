import sys
input=sys.stdin.readline

def GCD(a,b):
    if b%a: return GCD(b%a,a)
    else: return a

n,m= map(int,input().split(':'))
gcd = GCD(n,m)
print(n//gcd,end='')
print(':',end='')
print(m//gcd)
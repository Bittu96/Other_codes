from math import sqrt

def is_prime(num):
    for i in range(2,1+int(sqrt(num))):
        if num%i:
            continue
        else:
            return False
    return num


def check(l,r):
    lprime,rprime = None,None
    while l<=r:
        if lprime==None:
            if is_prime(l):
                lprime=l
            else: 
                l+=1
        elif rprime==None:
            if is_prime(r):
                rprime=r
            else:
                r-=1
        else: return lprime,rprime
        

def main():
    for _ in range(int(input())):
        l,r = list(map(int,input().split()))
        primes = check(l,r)
        print(primes[1]-primes[0] if primes is not None else -1 )

main()




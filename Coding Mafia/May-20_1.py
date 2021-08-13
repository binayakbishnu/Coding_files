def isprime(x):
    for j in range(2,(x//2)+1):
        if x%j == 0:
            return 0
    return 1

def primefactors(n):
    # return set of prime factors
    L = []
    for i in range(2,(n//2)+1):
        if n%i == 0 and isprime(i) == 1:
            L.append(i)
    
    if isprime(n):
        L.append(n)
    # print(L)
    return set(L)


n = int(input())
primes = set([int(i) for i in input().split()])

i=1
x=1

while i!=n:
    # print(x,primefactors(x))

    if primefactors(x).issubset(primes):
        i+=1
        # print(x,i)
        if i == n:
            break
    x+=1
    
print(x)

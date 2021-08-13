from math import comb

A = int(input("A: "))
X = int(input("X: "))
n = int(input("n: "))

S = 0

for i in range(n+1):
    c = comb(n,n-i)
    T = c*(A**(n-i))*(X**i)
    print(T,end=" ")
    S+=T

print()
print("Sum: ",S)

A = int(input("Area: "))

c =0

for L in range(1,A+1):
    for B in range(1,A+1):
        if L%2 == 0 and B%2 == 0 and L == B and L*B == A:
            c+=1
        elif L*B == A:
            c+=1

print(c)

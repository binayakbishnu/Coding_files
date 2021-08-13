n = input().split()
r = n[0]
c = n[1]

matrix = []

for r_ in range(int(r)):
    row = input().split()
    matrix.append(row)

# print(matrix)

for r_ in range(int(r)):
    m = 0
    c = 0
    rmax = 0
    for c_ in range(c):
        if L[r_][c_] == 1:
            c+=1
    if m<c:
        rmax = r_

print(r_+1)
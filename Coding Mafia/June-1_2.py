N = int(input())

matrix = []

for n in range(N):
    row = input().split()
    matrix.append(row)

for r_ in range(N):
    for c_ in range(r_+1,N):
        if c_!=r_:
            temp = matrix[r_][c_]
            matrix[r_][c_] = matrix[c_][r_]
            matrix[c_][r_] = temp

# print(matrix)

for n in range(N):
    print(matrix[n])
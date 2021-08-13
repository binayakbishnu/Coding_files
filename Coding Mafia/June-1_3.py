S = input()
N = int(input())

for n in range(N+1):
    print(bin(n)[2:])
    if str(bin(n))[2:] not in S:
        print("False")
        exit(0)

print("True")
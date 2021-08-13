L = input().split()
L = [int(i) for i in L]

####! See efficient solution

L.sort()
# print(L)

L1 = L[:len(L)//2+1]
L = L[len(L)//2+1:]

print(L1,L)

L2 = []

flag = 0
x,y=0,0
for i in range(len(L)+len(L1)):
    if flag == 0:
        L2.append(L1[x])
        x+=1
        flag =1
    elif flag == 1:
        L2.append(L[y])
        y+=1
        flag = 0

print(L2)


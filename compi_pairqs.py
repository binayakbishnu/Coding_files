n = int(input())
l = []
c = 0
for _ in range(n):
    l.append(int(input()))
#print(l)
i = 0
for i in range(len(l)):
    c=0
    #print(l[i])
    e=l[i]
    for p in range(1, e*(e-1)+1):
        for q in range(1, e*(e-1) + 1):
            a = ((q**p) - (p**q))
            #print(a)
            if a % e == 0:
                #print("Into if")
                c += 1
                


    print(c)
# demo
# 
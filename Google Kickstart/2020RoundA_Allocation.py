T = int(input())
for x in range(T):
    I = input().split()
    # print(I)
    N = int(I[0])
    B = int(I[1])
    L = input().split()
    L.sort()
    L = (int(x) for x in L)
    # print(L)
    count = 0
    cost = 0
    for i in L:
        # print(cost, cost+i)
        if cost+i <= B:
            cost += i
            count += 1
        else:
            break
    print("Case #{}: {}".format(x+1,count))

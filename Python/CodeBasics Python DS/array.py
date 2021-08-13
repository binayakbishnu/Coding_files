# Exercise
sales = [
    ["January", 2200],
    ["February", 2350],
    ["March", 2600],
    ["April", 2130],
    ["May", 2190],
]

print(sales[1][1]-sales[0][1])

print(sales[0][1]+sales[1][1]+sales[2][1])

for i in sales:
    if i[1] == 2000:
        print(i[0])

sales.append(["June",1980])

sales[3][1]-=200

print(sales)


# 2
n = int(input())

L=[]

for i in range(1,n+1,2):
    L.append(i)

print(L)
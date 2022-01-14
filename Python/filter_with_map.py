L = [4, 1, 63, 14, 67, 35, 76]
print(L)

print()
X = filter(lambda x: x % 2 == 0, L)
print(list(X))

print()
Y = map(lambda x: x*2, filter(lambda x: x % 2 == 0, L))
print(list(Y))

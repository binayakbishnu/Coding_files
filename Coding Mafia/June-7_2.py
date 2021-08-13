x = input()
x = [i for i in x]

for i in range(len(x)):
    if x[i] == '6':
        x[i] = '9'
        break

x = ''.join(x)
print(x)

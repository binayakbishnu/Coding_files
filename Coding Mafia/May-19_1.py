def func(n_):
    x = len(n_)
    for i in range(x):
        for j in range(x):
            print("index",i,j)
            print("element",n_[i],n_[j])
            if abs(i-j)==k and abs(n_[i]-n_[j])==t:
                return True
    
    return False


n = input().split()
n = [int(i) for i in n]

k = int(input()) # diff indices
t = int(input()) # diff elements

print(func(n))


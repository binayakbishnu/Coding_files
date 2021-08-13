array = input().split()
array = [int(i) for i in array]

c = 0
for i in range(len(array)-1):
    # print(array[i],array[i+1])
    if c>1:
        break
    if array[i]>array[i+1]:
        c+=1
        # print(c)

if c<=1:
    print("True")
else:
    print("False")
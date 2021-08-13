dict={}
list=[1,2,3,3,1,0]
for i in list:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1

for key,value in dict.items():
    print('Element {} Frequency:{}'.format(key,value))
print(dict)
list=[]
for key2,value2 in dict.items():
    if dict[i]==1:
        list.append(i)


print('Unique elements list',list)
list2=[]
for i in dict:
    if dict[i]>1:
        list2.append(i)

print('Duplicates elements list',list2)

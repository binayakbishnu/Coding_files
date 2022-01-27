class Overrider:
    def __init__(self,name,age,batch):
        self.name = name
        self.age = age
        self.batch = batch

    def __len__(self):
        # return 'Name: {},Age: {},Batch: {}'.format(len(self.name),len(str(self.age)),len(self.batch))
        return len(self.name)+len(str(self.age))+len(self.batch)

    def __str__(self):
        return ' '.join([self.name,str(self.age),self.batch])

o1 = Overrider('Binayak Bishnu', 19, '2020-24')

print(o1.__dict__)
print(len(o1))
print(o1)
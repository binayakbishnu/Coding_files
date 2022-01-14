class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first.lower() + '.' + last.lower() + '@company.com'

    @property
    # ^ therefore method can be accessed as an attribute and not a function
    # * therfore don't need to change instance codes [emp1.email() not required]
    def email(self):
        return self.first.lower() + '.' + self.last.lower() + '@company.com'

    @property
    def fullname(self):
        return self.first + ' ' + self.last

    @fullname.setter
    def fullname(self, name):
        # ^ other name applicable too
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        # ^ other name applicable too
        print('Delete name')
        self.first = None
        self.last = None


emp1 = Employee('Binayak', 'Bishnu', 30000)
emp2 = Employee('Test', 'User', 40000)

"""emp1.first = 'ABC'
print(emp1.first)
print(emp1.email)
print(emp1.fullname())
# * email didn't change """

# * now email changed without making it email() """


emp1.fullname = 'ABC DEF'
# ^ error even though made into @property, therefore need setter
# ^ also does not change first and last
print(emp1.__dict__)


del emp1.fullname
print(emp1.__dict__)


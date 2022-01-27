""" class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@company.com'

    def fullname(self):
        return self.first + ' ' + self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        # self.pay = int(self.pay * Employee.raise_amt)

    def __repr__(self):
        # * used for debugging and logging purposes
        return "Employee('{}', '{}','{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        # *used to display objects
        pass


emp1 = Employee('Binayak', 'Bishnu', 30000)
emp2 = Employee('Test', 'User', 40000)

print(emp1)  # *now doesn't just show vague object description"""


""" class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@company.com'

    def fullname(self):
        return self.first + ' ' + self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        # self.pay = int(self.pay * Employee.raise_amt)

    def __repr__(self):
        # * used for debugging and logging purposes
        return "Employee('{}', '{}','{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        # *used to display objects
        # *overrides __repr__ unless repr exclusively called
        return '{} - {}'.format(self.fullname(), self.email)


emp1 = Employee('Binayak', 'Bishnu', 30000)
emp2 = Employee('Test', 'User', 40000)

print(emp1)  # *now doesn't just show vague object description

print(repr(emp1))
print(str(emp1))

print(emp1.__repr__())
print(emp1.__str__()) """


print(int.__add__(1, 2))
# *dunder method of int class
print(str.__add__('a', 'b'))
# *dunder method of str class


""" class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@company.com'

    def fullname(self):
        return self.first + ' ' + self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        # self.pay = int(self.pay * Employee.raise_amt)

    def __add__(self, other):
        return self.pay + other.pay


emp1 = Employee('Binayak', 'Bishnu', 30000)
emp2 = Employee('Test', 'User', 40000)

print(emp1+emp2) """


print(len('test'))
print('test'.__len__())


class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@company.com'

    def fullname(self):
        return self.first + ' ' + self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        # self.pay = int(self.pay * Employee.raise_amt)

    def __len__(self):
        return len(self.fullname())-1


emp1 = Employee('Binayak', 'Bishnu', 30000)

print(len(emp1))
print(emp1.__len__())
print(len(emp1))    # as if it were len of list or string


class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@company.com'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        # self.pay = int(self.pay * Employee.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    #* changes class variable value to amount 

emp1 = Employee('Binayak', 'Bishnu',30000)
emp2 = Employee('Test', 'User', 40000)

print(emp1.raise_amt)
print(emp2.raise_amt)
print(Employee.raise_amt)

Employee.set_raise_amt(1.05)    # equivalent to Employee.raise_amt=1.05

print(emp1.raise_amt)
print(emp2.raise_amt)
print(Employee.raise_amt)

emp1.set_raise_amt(1.06)    # sets new value to all unlike emp1.raise_amt=1.06

print(emp1.raise_amt)
print(emp2.raise_amt)
print(Employee.raise_amt)
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

emp1 = Employee('Binayak', 'Bishnu',30000)
emp2 = Employee('Test', 'User', 40000)

# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)

# print(emp1.raise_amt)
# print(Employee.raise_amt)

# print(emp1.__dict__)
# print(Employee.__dict__)

Employee.raise_amt = 1.05
print(emp1.raise_amt)
print(emp1.__dict__)

emp1.raise_amt = 1.03
print(emp1.raise_amt)
print(emp1.__dict__)
#* since class variable of instacen changed, __dict__ of instance not contains class variable

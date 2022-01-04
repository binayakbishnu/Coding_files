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

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    #* does not take self or cls like above
    #* similar to normal functions
    # use when class/instance not used
    def is_weekend(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return True
        return False

emp1 = Employee('Binayak', 'Bishnu',30000)
emp2 = Employee('Test', 'User', 40000)

#! classmethods are alternative constructors 

""" print(emp1.raise_amt)
print(emp2.raise_amt)
print(Employee.raise_amt)

Employee.set_raise_amt(1.05)    # equivalent to Employee.raise_amt=1.05

print(emp1.raise_amt)
print(emp2.raise_amt)
print(Employee.raise_amt)

emp1.set_raise_amt(1.06)    # sets new value to all unlike emp1.raise_amt=1.06

print(emp1.raise_amt)
print(emp2.raise_amt)
print(Employee.raise_amt) """

emp1_str = 'John-Doe-7000'
emp2_str = 'Steve-Smith-30000'
emp3_str = 'Jane-Doe-90000'

# first, last, pay = emp1_str.split('-')
# new_emp1 = Employee(first, last, pay)
# print(new_emp1.__dict__)
#^ but sortof hardcoded
#* to make it automatic
new_emp1 = Employee.from_string(emp1_str)
print(new_emp1.__dict__)


import datetime
my_date = datetime.date(2020, 7, 11)
print(Employee.is_weekend(my_date))
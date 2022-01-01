""" class Employee:
    pass
#! empty class

emp1 = Employee()
emp2 = Employee()

print(emp1)
print(emp2)
#! instance variables """


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@company.com'

    def fullname(self):
        return self.first + ' ' + self.last


emp1 = Employee('Binayak', 'Bishnu',30000)
emp2 = Employee('Test', 'User', 40000)

print(emp1.first)
print(emp2.email)

print(emp1.fullname())
print(Employee.fullname(emp1))

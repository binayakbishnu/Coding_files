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


class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay)
        # ^ used in multiple inheritance
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        # ^ [] not passed as argument since mutable type
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())

# emp1 = Employee('Binayak', 'Bishnu',30000)
# emp2 = Employee('Test', 'User', 40000)


""" dev1 = Developer('Binayak', 'Bishnu', 30000)
dev2 = Developer('Test', 'User', 40000)

print(dev1.__dict__)
print(dev2.__dict__)

print(help(Developer)) """

dev1 = Developer('Binayak', 'Bishnu', 30000, 'Python')
dev2 = Developer('Test', 'User', 40000, 'Java')

# print(dev1.__dict__)

mgr1 = Manager('John', 'Doe', 90000, [dev1])
print(mgr1.email)
mgr1.print_emp()

mgr1.add_emp(dev2)
mgr1.print_emp()

# * is an instance of class or not
print(isinstance(mgr1,Employee))
print(isinstance(mgr1,Manager))
print(isinstance(mgr1,Developer))

# * is subclass or not
print(issubclass(Manager, Employee))

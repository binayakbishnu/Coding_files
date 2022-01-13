class Student:
    def __init__(self, name, yearofadmission, roll):
        self.name = name
        self.yearofadmission = yearofadmission
        self.roll = roll

    def application_no(self):
        name_broken = self.name.split(' ')
        initial = name_broken[0][0] + name_broken[1][0]
        applno = initial + self.roll
        return applno

class Core:
    def __init__(self,domain):
        self.domain = domain

class Fresher_Core(Student, Core):
    def __init_(self,)


student1 = Student('Binayak Bishnu', 2020, '20BIT0155')
print(student1.__dict__)
print(student1.application_no())

class Fresher:
    def __init__(self, name, yearofadmission, roll):
        self.name = name
        self.yearofadmission = yearofadmission
        self.roll = roll

    def application_no(self):
        name_broken = self.name.split(' ')
        self.applno = name_broken[0][0] + name_broken[1][0] + self.roll
        return self.applno

    def name_print_in_child(self):
        print(self.name)


class Core:
    def __init__(self, domain):
        self.domain = domain


class Fresher_Core(Fresher, Core):
    def __init__(self, name, yearofadmission, roll, domain):
        Fresher.__init__(self, name, yearofadmission, roll)
        Core.__init__(self, domain)

        Fresher.name_print_in_child(self)


fresher1 = Fresher('Binayak Bishnu', 2020, '20BIT0155')
print(fresher1.__dict__)
# print(fresher1.applno)    # error
print(fresher1.application_no())
print(fresher1.applno)
print(fresher1.__dict__)

print();print()

fresher2 = Fresher_Core('Neon Neo', 2021, '21BIT0000', 'Webdev')
print(fresher2.__dict__)
print(fresher2.yearofadmission)
print(fresher2.application_no())
print(fresher2.applno)
print(fresher2.__dict__)

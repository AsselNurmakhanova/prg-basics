class C:
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority
        if self.age < 18:
            self.total = self.surname.lower() + self.name[0].lower() + str(seniority)
        else:
            self.total = self.surname.upper() + self.name[0].upper() + str(seniority)

person1 = C("George","Brown",21,4)
print(person1.total)
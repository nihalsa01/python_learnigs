class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        return f"{self.firstname} {self.lastname} is {self.age} years old."

    def add_skill(self, skill):
        self.skills.append(skill)
        return self.skills

'''
p = Person('Nihal', 'Sayyad', 26, 'India', 'Pune')
print(p.person_info())

print(p.add_skill('Python'))
print(p.add_skill('C language'))
print(p.add_skill('Linux'))
'''
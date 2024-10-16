class Person:
    def __init__(self, firstname="john", lastname="mutembei", age=200, country="Kenya", city="Eldoret"):
        self.firstname = firstname 
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills=[]

    def person_info(self):
        return f'My name is {self.firstname} {self.lastname}. I am {self.age} years old. I live in {self.country}, {self.city} city. I have skills in{self.skills}'
    def add_skill(self, skill):
        self.skills.append(skill)

p1=Person()
print(p1.person_info())

p1.add_skill("HTml")
p1.add_skill("Python")
print(p1.person_info())


class Student(Person):
    super().__init__(self,firstname, lastname, age, country, city)

S1=Student("Elvira","Kerage",30,"kisii","Nyamira")
S1.skills.append("Cooking")
print(S1.person_info())
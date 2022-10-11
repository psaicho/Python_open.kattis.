class Body:
    def __init__(self, name, age, kilos):
        self.kilos = kilos
        self.name = name
        self.age = age

    def __add__(self, otherBody):
        total_age = (self.age + otherBody.age)
        total_kilos = (self.kilos + otherBody.kilos)
        common_name =(self.name + otherBody.name)
        return Body(common_name, total_age, total_kilos)


x = Body("Tomek", 39, 45)
y = Body("Adam", 45, 54)
t = x + y
print(t.name)




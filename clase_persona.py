class Persona:
    def __init__(self, name, age, street):
        self.name = name
        self.age = age
        self.street = street

    def description(self):
        print("name:", self.name, " age:", self.age, " street:", self.street)


class Employee(Persona):
    def __init__(self, salary, antiquity, name_employee, name_age, street):
        super().__init__(name_employee, name_age, street)
        self.salary = salary
        self.antiquity = antiquity

    def description(self):
        super().description()
        print("salary", self.salary, "antiquity", self.antiquity)


juan = Persona("juan", 25, "pintado")
juan.description()

pepe = Employee(300, 12, "pepe", 34, "mena")
pepe.description()

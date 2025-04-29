"""
CLASES EN PYTHON
"""


class Programmer:

    surname: str = None

    def __init__(self, name: str, age: int, languages: list):
        self.name = name
        self.age = age
        self.languages = languages

    def print(self):
        print(
            f"Nombre: {self.name} | Apellidos: {self.surname} | Edad: {self.age} | Lenguajes: {self.languages}"
        )


my_programmer = Programmer("Marlon", 36, ["Python", "Kotlin", "Swift"])
my_programmer.print()
my_programmer.surname = "Joel"
my_programmer.print()
my_programmer.age = 37
my_programmer.print()

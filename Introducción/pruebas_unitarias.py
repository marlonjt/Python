"""
Pruebas unitarias con python
"""

import unittest

from datetime import datetime, date


def sumar(n1, n2):
    if not isinstance(n1, (int, float)) or not isinstance(n2, (int, float)):
        raise ValueError("Solo admite  números no letras")
    return n1 + n2


print(f"la suma es: {sumar(2, 4)}")


class TestSuma(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(sumar(3, 4), 7)
        self.assertEqual(sumar(4, 4), 8)


"""
Extra
"""


class TestDict(unittest.TestCase):

    def setUp(self):
        self.data = {
            "name": "Tu nombre",
            "age": 24,
            "birth_date": datetime.strptime("03-02-00", "%d-%m-%y").date(),
            "programming_languages": ["Python", "JS", "TypeScript"],
        }

    def test_exits_dict(self):
        self.assertIn("name", self.data)
        self.assertIn("age", self.data)
        self.assertIn("birth_date", self.data)
        self.assertIn("programming_languages", self.data)

    def test_exist_fields(self):
        self.assertIsInstance(self.data["name"], str)
        self.assertIsInstance(self.data["age"], int)
        self.assertIsInstance(self.data["birth_date"], date)
        self.assertIsInstance(self.data["programming_languages"], list)


unittest.main()

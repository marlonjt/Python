"""
Método enumerate dentro de python y librería enum
"""

week = ["lunes", "martes", "miércoles ", "jueves", "viernes", "sábado", "domingo"]

for i, j in enumerate(week, 1):
    print(f"{i}.{j}")

"""
Sistema de pedidos 
"""


class SystemOrders:

    def state_orders(self):
        self.states = [
            "Pending",
            "Send",
            "Delivered",
            "Cancel",
        ]

    def update_state():
        pass

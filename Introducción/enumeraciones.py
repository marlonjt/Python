"""
Método enumerate dentro de python y librería enum
"""

from enum import Enum

week = ["lunes", "martes", "miércoles ", "jueves", "viernes", "sábado", "domingo"]

for i, j in enumerate(week, 1):
    print(f"{i}.{j}")


class Week(Enum):
    LUNES = 1
    MARTES = 2
    MIÉRCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SÁBADO = 6
    DOMING0 = 7


def week_day(number):
    print(f"Escogiste el día: {Week(number).name}")


week_day(7)
week_day(2)


"""
Sistema de pedidos 
"""


class OrderStatus(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3
    CANCELLED = 4


class Order:

    status = OrderStatus.PENDING

    def __init__(self, id) -> None:
        self.id = id

    def ship(self):
        if self.status == OrderStatus.PENDING:
            self.status = OrderStatus.SHIPPED
            self.display_status()
        else:
            print("El pedido ya ha sido enviado o cancelado")

    def deliver(self):
        if self.status == OrderStatus.SHIPPED:
            self.status = OrderStatus.DELIVERED
            self.display_status()
        else:
            print("El pedido necesita ser enviado antes de entregarse.")

    def cancel(self):
        if self.status != OrderStatus.DELIVERED:
            self.status = OrderStatus.CANCELLED
            self.display_status()
        else:
            print("El pedido no se puede cancelar ya que ya se ha entregado.")

    def display_status(self):
        print(f"El estado del pedido {self.id} es {self.status.name}")


order_1 = Order(1)
order_1.display_status()
order_1.deliver()
order_1.ship()
order_1.deliver()
order_1.cancel()

from enum import Enum
from datetime import datetime
import time
import random


def called(n):
    return n[0] * n[1]


def caller(func, n):
    return func(n)


# tuple
num = (8, 5)

ans = caller(called, num)

print("Multiplication =", ans)

"""
Extra pedidos
"""


class Estado_Pedido(Enum):
    EN_PROCESO = 1
    CONFIRMADO = 2
    CANCELADO = 3


class Pedido:

    def __init__(self, name: str):
        self.name = name
        self.status = Estado_Pedido.EN_PROCESO

    def pedidos(self, func):
        mensaje = func()
        print(f"{mensaje}")

    def mensaje_pedido(self):
        return f"El estado del plato {self.name} está {self.status.name}"

    def proceso_confirmación(self):
        if self.status != Estado_Pedido.CONFIRMADO:
            self.status = Estado_Pedido.CONFIRMADO
        return self.mensaje_pedido()


# Crear tres instancias de Pedido
plato1 = Pedido("encebollado")
plato2 = Pedido("cangrejo")
plato3 = Pedido("arroz con menestra")

# Lista de pedidos
platos = [plato1, plato2, plato3]

# Confirmar pedidos cada 5 segundos
for plato in platos:
    print(f"Inicio: {datetime.now()}, {plato.mensaje_pedido()}")
    plato.pedidos(plato.proceso_confirmación)
    proceso = random.randint(1, 10)
    time.sleep(proceso)

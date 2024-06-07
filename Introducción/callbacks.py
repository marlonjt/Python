from enum import Enum


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

    status = Estado_Pedido.EN_PROCESO

    def __init__(self, name: str):
        self.name = name

    def pedidos(self, func):
        mensaje = func()
        print(f"{mensaje}")

    def mensaje_pedido(self):
        return f"El estado del plato {self.name} está {self.status.name}"

    def proceso_confirmación(self):
        if self.status != Estado_Pedido.CONFIRMADO:
            self.status = Estado_Pedido.CONFIRMADO
        return self.mensaje_pedido()


plato = Pedido("encebollado")
plato.mensaje_pedido()
plato.pedidos(plato.proceso_confirmación)

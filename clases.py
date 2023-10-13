class Coche:
    def __init__(self):
        self.__color = "Rojo"
        self.__llantas = 4
        self.__precio = 250
        self.__encendido = False

    def prender(self, on):
        self.__encendido = on

        if(self.__encendido):
            chequeo =self.__estado()

        if(self.__encendido and chequeo):
            print('auto on')
        elif(self.__encendido and chequeo==False):
            print('auto off')

    def __estado(self):
        self.agua = "ok"
        self.gasolina = "ok"

        if (self.agua == "ok" and self.gasolina == "ok"):
            return True
        else:
            return False

auto = Coche()
print(auto.prender(True))


print("---------------------auto nuevo----------------------")
auto2 = Coche()
print(auto.prender(False))



import math

class Vehiculo:

    def __init__(self, vm: int, km: int):
        self.velocidad_maxima: int = vm
        self.kilometraje: int = km

class Punto:

    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def mostrar(self, x: int, y:int):
        return print(f"Las coordenadas del punto son: X = {x}, Y = {y}")

    def mover(self, x: int, y: int):
        self.x = x
        self.y = y
        return
    def calcular_distancia(self, x: int, y: int, distancia: int, otro_punto: int):
        distancia = math.sqrt((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2)
        return distancia

class Rectangulo:

    def __init__(self, esquina1: int,esquina2: int ):
        self.esquina1: int = esquina1
        self.esquina2: int = esquina2

    def perimetro(self, esquina1: int, esquina2: int) -> int:


    def area(self, esquina1: int, esquina2: int) -> int:


    def determinar_cuadrado(self, esquina1:int, esquina2: int) -> int:


class Circulo:

    def __init__(self,centro: float, radio: float):
        self.centro: float = centro
        self.radio: float = radio

    def area(self, centro: float, radio: float) -> float:

    def perimetro(self, centro: float, radio: float) -> float:

    def determinar_pertenencia(self, centro: float, radio: float) -> float:


class Carta:

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta


class CuentaBancaria:

    def __init__(self, numero_cuenta: int, propietarios, balance : int ):
        self.numero_cuenta: int = numero_cuenta
        self.propietarios = propietarios
        self.balance: int = balance

    def depositar(self) -> float:

    def retirar(self) -> float:

    def aplicar_cuota_manejo(self) -> float:

    def detalles(self) -> float:







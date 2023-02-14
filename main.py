
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

    def __init__(self, base: int,altura: int ):
        self.base: int = esquina1
        self.altura: int = esquina2

    def perimetro(self, base: int, altura: int) -> int:
        perimetro = (2*base) + (2*altura)
        return print(f"El perímetro es: {perimetro}")


    def area(self, base: int, altura: int) -> int:
        self.area = (base * altura)
        return print(f"El area es: {area}")


    def determinar_cuadrado(self, base:int, altura: int) -> int:
        if base == altura:
         return print(f"El rectángulo es un cuadrado")


class Circulo:

    def __init__(self,centro: float, radio: float):
        self.centro: float = centro
        self.radio: float = radio

    def area(self, centro: float, radio: float) -> float:
        self.area = math.pi * (radio)**2
        return print(f"El area del circulo es: {area}")

    def perimetro(self, centro: float, radio: float) -> float:
        perimetro = (2 * math.pi * radio)
        return(f"El perimetro del circulo es: {perimetro}")

    def determinar_pertenencia(self, centro: float, radio: float) -> float:
        determinar_pertenencia =


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







"""Cree una clase Vehículo que contenga los atributos de instancia velocidad_maxima y kilometraje.
Cree una clase Punto que represente un punto en el plano cartesiano.
A la clase del punto anterior, defínale los siguientes métodos:
- Un método mostrar que imprima por consola las coordenadas del punto
- Un método mover que cambie las coordenadas del punto
- Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.
Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los puntos que definen sus esquinas. Agregue métodos a la clase Rectángulo para calcular su perímetro, calcular su área e indicar si el rectángulo es un cuadrado.
Cree una clase Circulo que tenga las propiedades centro y radio, las cuales se inicializan con parámetros en el constructor. Defina métodos en la clase para calcular el área, el perímetro e indicar si un punto pertenece al círculo o no.
Cree una clase Carta que contenga dos propiedades valor y pinta, las cuales son asignadas solo al momento de la construcción del objeto (se pasan como parámetros en el constructor). Defina 4 constantes que representan los nombres de las 4 pintas que puede tener una carta.
Cree una clase CuentaBancaria que contenga los siguientes atributos: numero_cuenta, propietarios y balance. Los tres atributos se deben inicializar en el constructor con valores recibidos como parámetros.
Para la clase CuentaBancaria, cree un método depositar que maneje las acciones de depósito en la cuenta.
Para la clase CuentaBancaria, cree un método retirar que maneje las acciones de retiro de la cuenta.
Para la clase CuentaBancaria, cree un método aplicar_cuota_manejo que aplique un porcentaje del 2% sobre el balance de la cuenta
Para la clase CuentaBancaria, cree un método mostrar_detalles que imprima por consola los detalles de la cuenta bancaria."""
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
        return print(f"Las nuevas coordenadas son: X={x}, Y={y}")
    def calcular_distancia(self, x: int, y: int, distancia: int, otro_punto: int):
        self.distancia = math.sqrt((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2)
        return print(f"La distancia entre los puntos es: {distancia}")

class Rectangulo:
    def __init__(self, base: int,altura: int ):
        self.base: int = base
        self.altura: int = altura
    def perimetro(self, base: int, altura: int) -> int:
        perimetro = 2 * (base+altura)
        return print(f"El perímetro es: {self.perimetro}")
    def area(self, base: int, altura: int) -> int:
        self.area = (base * altura)
        return print(f"El area es: {self.area}")
    def determinar_cuadrado(self, base:int, altura: int) -> int:
        if base == altura:
         return print(f"El rectángulo es un cuadrado")

class Circulo:
    def __init__(self, centro: Punto, radio: float):
            self.centro: Punto = centro
            self.radio: float = radio
    def area(self) -> float:
        area = math.pi * (self.radio) ** 2
        return print(f"El area del circulo es: {area}")
    def perimetro(self) -> float:
        perimetro = (2 * math.pi * self.radio)
        return (f"El perimetro del circulo es: {perimetro}")
    def determinar_pertenencia(self, punto: Punto):
        distancia = self.centro.calcular_distancia(punto)
        return distancia <= self.radio
class Carta:
    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta
        PINTAS = ["Corazones", "Treboles", "Diamantes", "Picas"]
    def pintas_carta(self,valor,pinta):
        self.valor = valor
        self.pinta = pinta

class CuentaBancaria:
    def __init__(self, numero_cuenta: int, propietarios: int, balance : float ):
        self.numero_cuenta: int = numero_cuenta
        self.propietarios: int = propietarios
        self.balance: float = balance
    def depositar(self, cantidad) -> float:
        self.depositar = float(input("Ingrese cuanto dinero quiere depositar: "))
        self.balance += cantidad
        return print(f"Ha depositado: ${self.depositar}")
    def retirar(self,balance: float) -> float:
        self.retirar = float(input("Ingrese cuanto dinero quiere retirar: "))
        if self.retirar > self.balance:
           print("No tienes tanto dinero para retirar")
        else: self.balance - self.retirar
        return print(f"Ha retirado: ${self.retirar}, ahora tienes: ${self.balance}")
    def aplicar_cuota_manejo(self, balance: float) -> float:
        self.aplicar_cuota_manejo = self.balance * 0.02
        return print(f"La cuota de manejo es de: ${self.aplicar_cuota_manejo}")
    def detalles(self, numero_cuenta: int, propietarios: int, balance: float) -> float:
        print(f"El numero de cuenta es: {self.numero_cuenta}")
        print(f"Propietarios: {self.propietarios}")
        print(f"El balance de su cuenta es: {self.balance}")







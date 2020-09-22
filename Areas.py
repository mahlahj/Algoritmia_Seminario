import math
import os

class Areas:
    def triangulo (self, base, altura):
        return base * altura/2
    
    def cuadrado (self, lado):
        return lado ** 2
    
    def circulo (self, radio):
        return math.pi * (radio ** 2)

def menu():
    area = Areas()

    while(True):
        print("1.- Triangulo.\n2.- Cuadrado.\n3.- Circulo.\n4.- Salir.")
        opc = (input("Selecciona una opción: "))
        if opc == '1':
            base = float(input("Dame la base: "))
            altura = float(input("Dame la altura: "))
            area.triangulo(base, altura)
            print ("El area es: ", area.triangulo(base, altura))
        elif opc == '2':
            lado = float(input("Dame el lado: "))
            area.cuadrado(lado)
            print ("El area es: ", area.cuadrado(lado))
        elif opc == '3':
            radio = float(input("Dame el radio: "))
            area.circulo(radio)
            print ("El area es: ", area.circulo(radio))
        elif opc == '4':
            print("Adios.")
            break
        else:
            print("Opcion invalida.")
        
        input("Presiona 'enter' para continuar.")
        os.system("cls")

menu()
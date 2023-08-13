"""
Calculating circle area
"""
# import math
from math import pi

if __name__ == "__main__":
    raioStr = input("Informe o raio: ")
    raio = float(raioStr)
    area_circulo = pi * (raio ** 2)

    print(f'A área do círculo é: {area_circulo}')

    print(f'Nome do modulo:', __name__)
    print(f'Nome do pacote:', __package__)

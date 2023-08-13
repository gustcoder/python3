"""
Calculating circle area
"""
# import math
from math import pi


def circle_area(raio):
    return pi * (raio ** 2)


if __name__ == "__main__":
    raioStr = input("Informe o raio: ")
    area_circulo = circle_area(float(raioStr))

    print(f'A área do círculo é: {area_circulo}')

    print(f'Nome do modulo:', __name__)
    print(f'Nome do pacote:', __package__)

"""
Calculating circle area
"""
# import math
from math import pi
import sys


def circle_area(raio):
    return pi * (raio ** 2)


if __name__ == "__main__":
    raioStr = sys.argv[1]  # recebe parametro direto via comando - executar nome do arquivo + valor do raio
    area_circulo = circle_area(float(raioStr))

    print(f'A área do círculo é: {area_circulo}')

    print(f'Nome do modulo:', __name__)
    print(f'Nome do pacote:', __package__)

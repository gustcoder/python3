"""
Calculating circle area
"""
# import math
from math import pi
import sys
import errno


def show_help(text, parameter=None):
    print(text.format(parameter)) if parameter else print(text)


def circle_area(raio):
    return pi * (raio ** 2)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_help("É necessário informar {} <raio>", sys.argv[0])
        # sys.exit(0) - terminou com sucesso
        # sys.exit(1) - terminou com erro, que é o mesmo que EPERM
        sys.exit(errno.EPERM) # importando errno podemos passar o tipo de erro especifico
        print("Já não passa mais aqui!")
    elif not sys.argv[1].isnumeric():
        show_help("<raio> precisa ser numérico!")
    else:
        raioStr = sys.argv[1]  # recebe parametro direto via comando - executar nome do arquivo + valor do raio
        area_circulo = circle_area(float(raioStr))

        print(f'A área do círculo é: {area_circulo}')

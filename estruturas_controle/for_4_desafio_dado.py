from random import randint


def sortear_dado() -> int:
    return randint(1, 6)


resultado_dado = sortear_dado()
for i in range(1, 7):
    if i % 2 != 0:  # i % 2 == 1 tambem dá certo
        continue
    elif (i % 2 == 0) and i == resultado_dado:
        print(f'ACERTOOOU! Número sorteado: {resultado_dado}')
        break
else:
    print(f'Não acertou o número! Número sorteado: {resultado_dado}')

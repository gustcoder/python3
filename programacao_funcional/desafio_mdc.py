def debug(menor, maior, i):
    print(f'{menor} % {i} = {menor % i} and {maior} % {i} = {maior % i}')

def mdc(numeros):
    menor = min(numeros)
    maior = max(numeros)
    mdc = menor
    i = menor
    while i > 1:
        # debug(menor, maior, i)
        if menor % i == 0 and maior % i == 0:
            mdc = i
        i -= 1
    return f'O MDC entre {numeros} é: {mdc}'


if __name__ == '__main__':
    print(mdc([21, 7]))
    print(mdc([125, 40]))
    print(mdc([55, 22]))
    print(mdc([15, 150]))
    print(mdc([7, 9]))

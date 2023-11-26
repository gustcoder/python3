# 0, 1, 1, 2, 3, 5, 8, 13, 21


def sum_last_two_values(resultado: list):
    return sum(resultado[-2:])


def fibonacci(limit: int):
    resultado = [0, 1]
    while resultado[-1] < limit:
        resultado.append(sum_last_two_values(resultado))
    return resultado


if __name__ == "__main__":
    limit = input("Informe o limite para o Fibonacci: ")
    print(fibonacci(int(limit)))


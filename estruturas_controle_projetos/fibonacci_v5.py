# 0, 1, 1, 2, 3, 5, 8, 13, 21

def fibonacci(limit: int):
    resultado = [0, 1]
    while resultado[-1] < limit:
        resultado.append(resultado[-2] + resultado[-1])
    return resultado


if __name__ == "__main__":
    limit = input("Informe o limite para o Fibonacci: ")
    print(fibonacci(int(limit)))


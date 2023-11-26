def fibonacci(quantity: int, sequency: tuple = (0, 1)):
    # condicao de parada
    if len(sequency) == quantity:
        return sequency
    sequency_tuple = (sum(sequency[-2:]),)  # para caracterizer a tupla, uma virgula deve ser explicitada

    return fibonacci(quantity, sequency + sequency_tuple)


if __name__ == "__main__":
    # Listar os 20 primeiros elementos da sequencia Fibonacci
    # print(type(fibonacci(20))) => uma tupla
    for fib in fibonacci(20):
        print(fib)


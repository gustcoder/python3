# 0, 1, 1, 2, 3, 5, 8, 13, 21

def fibonacci(limit: int):
    start = 0
    last = 1
    fibonacci = ''
    while last <= limit:
        current = start + last

        start = last
        last = current

        fibonacci += str(current) + ', '

    length = len(fibonacci)
    print(f'Fibonacci: 0, {fibonacci[0:length-2]}')


if __name__ == "__main__":
    limit = input("Informe o limite para o Fibonacci: ")
    fibonacci(int(limit))


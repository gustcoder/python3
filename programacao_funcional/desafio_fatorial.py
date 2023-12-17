def fatorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        i += i
    return result


def fatorial_curso(n):

    return (n * fatorial(n-1)) if n > 1 else 1


if __name__ == "__main__":
    print(f'10! = {fatorial(10)}')
    print(f'10! = {fatorial_curso(10)}')


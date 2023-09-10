def faixa_etaria(age: int) -> str:
    if 0 <= age < 18:
        return "Menor de Idade"
    elif age in range(18, 65):
        return "Adulto"
    elif age in range(65, 100):
        return "Melhor idade"
    elif age >= 100:
        return "Centenário"
    else:
        return "Idade inválida"


if __name__ == "__main__":
    for idade in (17, 35, 87, 11, -2):
        print(f'{idade}: {faixa_etaria(idade)}')

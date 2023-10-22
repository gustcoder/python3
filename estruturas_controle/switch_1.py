def get_days_week(selected_day):
    dias = {
        1: "Domingo",
        2: "Segunda",
        3: "Terça",
        4: "Quarta",
        5: "Quinta",
        6: "Sexta",
        7: "Sábado"
    }

    return dias.get(selected_day, "** inválido **")


if __name__ == "__main__":
    for day in range(0, 9):
        print(f' {day}: {get_days_week(day)}')


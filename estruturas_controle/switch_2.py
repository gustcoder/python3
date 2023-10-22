def check_is_weekend(selected_day):
    days = {
        1: "Domingo",
        2: "Segunda",
        3: "Terça",
        4: "Quarta",
        5: "Quinta",
        6: "Sexta",
        7: "Sábado"
    }

    day_returned = days.get(selected_day, "** inválido **")
    if day_returned == "Segunda" or day_returned == "Terça" or day_returned == "Quarta"\
            or day_returned == "Quinta" or day_returned == "Sexta":
        return "Dia de Semana"
    elif day_returned == "Sábado" or day_returned == "Domingo":
        return "Fim de Semana"
    else:
        return "** inválido **"


if __name__ == "__main__":
    for day in range(8):  # de 0 a 8
        print(f' {day}: {check_is_weekend(day)}')


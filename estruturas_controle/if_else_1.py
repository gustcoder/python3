# Conceitos     Notas
# A             De 10,0 a 9,1
# A-            De 9,0 a 8,1
# B             De 8,0 a 7,1
# B-            De 7,0 a 6,1
# C             De 6,0 a 5,1
# C-            De 5,0 a 4,1
# D             De 4,0 a 3,1
# D-            De 3,0 a 2,1
# E             De 2,0 a 1,1
# E-            De 1,0 a 0,0
# Para notas maiores que 10 e menores que 0, nota inválida


def show_note(note_value: str) -> str:
    concept = "Conceito: "
    if 10 >= float(note_value) >= 9.1:
        concept += "A"
    elif 9 >= float(note_value) >= 8.1:
        concept += "A-"
    elif 8 >= float(note_value) >= 7.1:
        concept += "B"
    elif 7 >= float(note_value) >= 6.1:
        concept += "B-"
    elif 6 >= float(note_value) >= 5.1:
        concept += "C"
    elif 5 >= float(note_value) >= 4.1:
        concept += "C-"
    elif 4 >= float(note_value) >= 3.1:
        concept += "D"
    elif 3 >= float(note_value) >= 2.1:
        concept += "D-"
    elif 2 >= float(note_value) >= 1.1:
        concept += "E"
    elif 1 >= float(note_value) >= 0.0:
        concept += "E-"
    else:
        concept = "Nota inválida! Valores devem ser entre 0 e 10."

    return concept


if __name__ == "__main__":
    note = input("Informe a nota: ")
    print(show_note(note))

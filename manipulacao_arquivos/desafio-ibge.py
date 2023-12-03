# usar enconding ISO-8859-1 (latin1)
# extrair o nono e o quarto campos
# ignorar a primeira linha

import csv


with open('desafio-ibge.csv', encoding='latin1') as file: # encoding
    with open('desafio-ibge.txt', 'w') as output:
        reader = csv.reader(file)
        for record in reader:
            if reader.line_num == 1:  # ignorando a primeira linha
                continue
            nome_orige = record[3]  # quarto campo
            nome_desti = record[8]  # nono campo
            print(f"nome_orige: {nome_orige}, nome_desti: {nome_desti}", file=output)


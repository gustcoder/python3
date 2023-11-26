file = open("pessoas.csv")
try:
    #  nesta versao o .strip() remove  os espacos em branco e consequentemente linhas em branco (vide resultado V2)
    for record in file:  # le linhas sob demanda, mais performantico relacionado ao V1 (stream)
        print('Nome: {}, Idade: {}'.format(*record.strip().split(',')))  # "*" para usar os itens da lista como argumentos do format
finally:
    file.close()


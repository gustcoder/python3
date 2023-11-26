file = open("pessoas.csv")
for record in file:  # le linhas sob demanda, mais performantico relacionado ao V1 (stream)
    print('Nome: {}, Idade: {}'.format(*record.split(',')))  # "*" para usar os itens da lista como argumentos do format
file.close()


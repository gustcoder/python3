with open("pessoas.csv") as file:
    #  nesta versao o .strip() remove  os espacos em branco e consequentemente linhas em branco (vide resultado V2)
    for record in file:  # le linhas sob demanda, mais performantico relacionado ao V1 (stream)
        print('Nome: {}, Idade: {}'.format(*record.strip().split(',')))  # "*" para usar os itens da lista como argumentos do format
if file.closed:
    print("Com o with, o arquivo (e até conexoes) será fechado automaticamente!")


file = open("pessoas.csv")
data = file.read()  # le o arquivo completo alocando na memoria
file.close()

for record in data.splitlines():
    print('Nome {}, Idade {}'.format(*record.split(',')))  # "*" para usar os itens da lista como argumentos do format


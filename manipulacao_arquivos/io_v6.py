with open("pessoas.csv") as file:
    with open('pessoas.txt', 'w') as output:
        for record in file:  # le linhas sob demanda, mais performantico relacionado ao V1 (stream)
            people = record.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*people), file=output)
if file.closed:
    print("Com o with, o arquivo (e até conexoes) será fechado automaticamente!")

if output.closed:
    print("Com o with, o arquivo (e até conexoes) será fechado automaticamente!")
import csv

# utilizando facilitador de lib CSV
with open('pessoas.csv') as file:
    for record in csv.reader(file):
        print("Nome: {}, Idade: {}".format(*record)) # aqui nao precisa de tratamento strip() e split()

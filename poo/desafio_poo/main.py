class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def is_adult(self):
        return self.idade >= 18


class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario=1500):
        super().__init__(nome, idade)
        self.salario = salario


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []

    def registrar_compra(self, compra):
        self.compras.append(compra)

    def data_ultima_compra(self):
        if len(self.compras) == 0:
            return 'Cliente não possui compras'
        try:
            return self.compras[-1]['data']
        except:
            print('Data não informada')

    def total_compras(self):
        total = 0
        for compra in self.compras:
            total += compra['valor']
        return total


class Compra:
    def __init__(self, vendedor, data, valor):
        self.vendedor = vendedor
        self.data = data
        self.valor = valor
        self.compra = {
            'vendedor': self.vendedor,
            'data': self.data,
            'valor': self.valor,
        }


if __name__ == "__main__":
    pessoa1 = Pessoa('Vendson da Silva', 40)
    pessoa2 = Pessoa('Clientson Pereira', 22)

    vendedor = Vendedor(pessoa1.nome, pessoa1.idade, salario=2500)
    cliente = Cliente(pessoa2.nome, pessoa2.idade)

    compra1 = Compra(vendedor.nome, '08/12/2023', 5000)
    cliente.registrar_compra(compra1.compra)

    compra2 = Compra(vendedor.nome, '10/12/2023', 2500)
    cliente.registrar_compra(compra2.compra)

    data_ultima_compra = cliente.data_ultima_compra()
    total = cliente.total_compras()

    print(f'Vendedor É Maior de Idade: {vendedor.is_adult()}')
    print(f'Cliente É Maior de Idade: {cliente.is_adult()}')
    print(f'Data Última Compra: {data_ultima_compra}')
    print(f'Total Compras: {total}')





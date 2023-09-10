produto = {'nome': 'Playstation 5', 'preco': 3999, 'estoque': 300}

for chave in produto:  # produto.keys() tambem pode ser usado
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(chave, '=', valor)

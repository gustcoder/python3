FORBIDDEN_WORDS = {'dark', 'elden', 'sekiro'}
texts = [
    'Não jogarei a DLC do Elden Ring',
    'Hoje eu zero Rise of the Tomb Raider!',
    'Sekiro só em 2025',
    'Estou curtindo Ghost of Tsushima',
    'Jogarei Dark Souls 2 de novo quando fizerem o remake'
]

for text in texts:
    created_set = set(text.lower().split())  # aqui cria-se um dict com cada palavra dos textos
    intersection = FORBIDDEN_WORDS.intersection(created_set)
    if intersection:
        print(f'O texto possui pelo menos uma das palavras proibidas: "{intersection}"')
    else:
        print(f'Texto autorizado: {text}')


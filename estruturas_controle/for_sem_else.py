FORBIDDEN_WORDS = ('futebol', 'religião', 'política')  # por convencao do PEP8, constantes com letras maiusculas
texts = [
    'João gosta de futebol e política',
    'A praia foi divertida'
]

for text in texts:
    found = False
    for word in text.lower().split():
        if word in FORBIDDEN_WORDS:
            print(f'O texto possui pelo menos uma das palavras proibidas: "{word}"')
            found = True
            break
    if not found:
        print(f'Texto autorizado: {text}')

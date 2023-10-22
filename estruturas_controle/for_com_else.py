FORBIDDEN_WORDS = ('futebol', 'religião', 'política', 'sekiro')  # por convencao do PEP8, constantes maiusculas
texts = [
    'João gosta de futebol e política',
    'Rise of the Tomb Raider é um jogão!',
    'Sekiro só em 2025 KKKK'
]

for text in texts:
    for word in text.lower().split():
        if word in FORBIDDEN_WORDS:
            print(f'O texto possui pelo menos uma das palavras proibidas: "{word}"')
            break
    else:
        print(f'Texto autorizado: {text}')

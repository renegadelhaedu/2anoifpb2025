def contarAlices(lista_presentes):
    contagem = 0
    for pessoa in lista_presentes:
        if 'alice' in pessoa:
            contagem = contagem + 1

    return contagem

def inserir_alunos():
    alunos = []
    resposta = 'sim'
    while resposta == 'sim':
        nome = input('digite o nome')
        alunos.append(nome)
        resposta = input('voce deseja continuar adicionando alunos?')

    return alunos


print('agora você vai preencher a lista com alunos do PRIMEIRO ano')
primeiro_ano = inserir_alunos()
print('agora você vai preencher a lista com alunos do SEGUNDO ano')
segundo_ano =  inserir_alunos()
print('agora você vai preencher a lista com alunos do TERCEIRO ano')
terceiro_ano = inserir_alunos()

qtdeano1 = contarAlices(primeiro_ano)
qtdeano2 = contarAlices(segundo_ano)
qtdeano3 = contarAlices(terceiro_ano)


if qtdeano1 > 0:
    print(f'hoje no primeiro no em sala tinham {qtdeano1} alices')

if qtdeano2 > 0:
    print(f'hoje no segundo ano em sala tinham {qtdeano2} alices')

if qtdeano3 > 0:
    print(f'hoje no terceiro ano em sala tinham {qtdeano3} alices')
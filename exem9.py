def contarAlices(lista_presentes):
    contagem = 0
    for pessoa in lista_presentes:
        if 'alice' in pessoa:
            contagem = contagem + 1

    return contagem

primeiro_ano = ['jose','pedro','talita']
segundo_ano = ['cecilia','fran','david','maria alice','analice']

qtdeano1 = contarAlices(primeiro_ano)
qtdeano2 = contarAlices(segundo_ano)

if qtdeano1 > 0:
    print(f'hoje no primeiro no em sala tinham {qtdeano1} alices')

if qtdeano2 > 0:
    print(f'hoje no segundo ano em sala tinham {qtdeano2} alices')
#precisa importar a classe Aluno? Nao
def fazer_login(lista, matricula, senha):

    for aluno in lista:
        if aluno.matricula == matricula and aluno.senha == senha:
            return aluno
    return None


def oi():
    return 'e toda vez que vc me disser oi, eu vou responder so oi'

def mostrar_menu_aluno(nome):
    print('\n\nSEJA BEM-VINDO', nome)
    print('1-cadastrar uma acao')
    print('2-remover uma acao')
    print('3-listar as acoes')
    print('4-sair')

    op2 = int(input('qual a opcao escolhida '))
    return op2
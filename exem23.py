from modelos.aluno import Aluno
from utilidades.login import fazer_login, oi, mostrar_menu_aluno

lista_alunos = []

while True:

    print('1-cadastrar aluno')
    print('2-login aluno')
    print('0-sair')

    op = int(input('digite a opcao desejada'))

    if op == 1:
        nome = input('digite seu nome')
        matricula = input('digite sua matricula')
        turma = input('digite sua turma')
        senha = input('digite sua senha')

        novo_aluno = Aluno(nome,matricula,turma,senha)
        lista_alunos.append(novo_aluno)
        print('aluno cadastrado com sucesso')

    elif op == 2:
        mat = input('digite sua matricula')
        senha = input('digite sua senha')

        aluno_logado = fazer_login(lista_alunos, mat, senha)
        if aluno_logado:
            while True:

                escolha = mostrar_menu_aluno(aluno_logado.nome)
                if escolha == 1:
                    acao = input('coloque as descricao da sua acao: ')
                    data = input('informe a data que ocorreu a acao')
                    aluno_logado.incluir_acao(acao, data)
                elif escolha == 3:
                    aluno_logado.listar_acoes()
                elif escolha == 4:
                    break
        else:
            print('matricula ou senha incorretas')


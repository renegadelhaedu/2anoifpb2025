class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.nota = 0

    def obter_informacoes(self):
        print(f"\n--- Informações do Aluno ---")
        print(f"Nome: {self.nome}")
        print(f"Matrícula: {self.matricula}")
        print(f"Nota: {self.nota:.1f}")




alunos = []
matriculas_utilizadas = list()

while True:
    print("\n" + "=" * 50)
    print("SISTEMA DE GESTÃO DE ALUNOS")
    print("=" * 50)
    print("1 - Cadastrar novo aluno")
    print("2 - Atribuir nota a um aluno")
    print("3 - Exibir informações de todos os alunos")
    print("4 - Exibir situação de um aluno específico")
    print("5 - Sair")
    print("=" * 50)

    opcao = input("Escolha uma opção (1-5): ")

    if opcao == "1":
        print("\n Vamos  CADASTRAR NOVO ALUNO ---")
        nome = input("Digite o nome do aluno: ")

        matricula = int(input("Digite o número de matrícula: "))
        if matricula in matriculas_utilizadas:
            print("Nao pode pois esta matrícula já está em uso")
        else:
            novo_aluno = Aluno(nome, matricula)
            alunos.append(novo_aluno)
            matriculas_utilizadas.append(matricula)
            print(f"Aluno {nome} cadastrado com sucesso! Matrícula: {matricula}")

    elif opcao == "2":
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado ainda!")
        else:
            print("\n--- ATRIBUIR NOTA ---")
            print("Alunos cadastrados:")
            i = 0
            for aluno in alunos:
                print(f"{i} -{aluno.nome} (Matrícula: {aluno.matricula})")
                i+=1

            indice = int(input("Digite o número do aluno: "))
            if 0 <= indice and indice < len(alunos):
                nova_nota = float(input("Digite a nova nota (0.0 a 10.0): "))
                alunos[indice].atribuir_nota(nova_nota)

            else:
                print("Número de aluno inválido!")

    elif opcao == "3":
        if len(alunos) == 0 :
            print("Nenhum aluno cadastrado ainda!")
        else:

            print("\n--- INFORMAÇÕES DE TODOS OS ALUNOS ---")
            for aluno in alunos:
                aluno.obter_informacoes()
                print('---- \n -----')

    elif opcao == "4":
        print('construa ')
    elif opcao == "5":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida! Digite um número entre 1 e 5.")


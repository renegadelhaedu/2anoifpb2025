from modelos import Pessoa
from dao import PessoaDAO

#instanciando um objeto DAO
daopessoa = PessoaDAO("pessoas.db")


#CONTROLE / regras / front do usuário
while True:
    print("\n1 - Inserir")
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Deletar")
    print("5 - Sair")
    op = input("Escolha: ")

    if op == "1":
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        if idade > 0 and idade < 130:
            #objeto instanciado do meu modelo
            nova_pessoa = Pessoa(None, nome, idade)
            #DAO
            dao.inserir(nova_pessoa) #mandando um objeto da classe Pessoa
            print('usuário cadastrado com sucesso')
        else:
            print('voce digitou errado')

    elif op == "2":
        lista_Objetos_pessoas = dao.listar()
        for p in lista_Objetos_pessoas:
            print(f'ID: {p.id}  | Nome: {p.nome} | Idade: {p.idade}')

    elif op == "3":
        id = int(input("ID para atualizar: "))
        nome = input("Novo nome: ")
        idade = int(input("Nova idade: "))
        p = Pessoa(id, nome, idade)
        dao.atualizar(p)

    elif op == "4":
        id = int(input("ID para deletar: "))
        dao.deletar(id)

    elif op == "5":
        break
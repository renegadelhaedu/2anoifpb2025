class Pessoa:
    nacionalidade = 'brasileiro'
    def __init__(self, nome, login, senha):
        self.__nome = nome
        self.login = login
        self.__senha = senha

    #uso isso para fazer o acesso (get) deste atributo
    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, nova_senha):
        if len(nova_senha) >= 8:
            self.__senha = nova_senha
        else:
            print('senha muito pequena. precisa ter 8 caracteres')

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        if len(novo_nome) >= 3:
            self.__nome = novo_nome
        else:
            print('nome muito pequeno. precisa ter pelo menos 3 caracteres')

    def mostrar_credencial(self):
        print(f'Meu nome é {self.nome}')
        print(f'e meu login é {self.login}')

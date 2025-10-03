class Aluno:
    def __init__(self, nome, matricula,turma,senha):
        self.__nome = nome
        self.__matricula = matricula
        self.__turma = turma
        self.__senha = senha
        self.__acoes = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    def incluir_acao(self, acao, data):
        if acao not in self.__acoes:
            self.__acoes.append([acao, data])
            print('acao cadastrada com sucesso')
        else:
            print('essa acao já estava cadastrada')

    def listar_acoes(self):
        print('\nMINHAS ACOES')
        for acao in self.__acoes:
            print(f'{acao[1]} - {acao[0]}')

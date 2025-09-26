#ENCAPSULAMENTO usando property
class Trabalhador:
    #atributo da classe
    ch_max = 44

    #construtor
    def __init__(self, nct, ch, nome, cpf):
        #atributos da instância/objeto
        self.nct = nct
        self.ch = ch
        self.__nome = nome
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.lower()

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        cpf = cpf.replace('.','')
        cpf = cpf.replace('-','')
        if len(cpf) == 11 and cpf.isnumeric():
            self.__cpf = cpf
        else:
            print('seu cpf nao está no padrão correto')

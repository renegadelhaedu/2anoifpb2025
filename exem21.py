#ENCAPSULAMENTO
class Trabalhador:
    #atributo da classe
    ch_max = 44

    #construtor
    def __init__(self, nct, ch, nome, cpf):
        self.nct = nct
        self.ch = ch
        self.__nome = nome
        self.__cpf = cpf

    def set_cpf(self,cpf):
        cpf = cpf.replace('.','')
        cpf = cpf.replace('-','')
        if len(cpf) == 11 and cpf.isnumeric():
            self.__cpf = cpf
        else:
            print('seu cpf nao está no padrão correto')

    def get_cpf(self):
        return self.__cpf

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
            self.__nome = novo_nome

rene = Trabalhador('1231234','40','rene de sousa','12345678910')
mariz = Trabalhador('453234', '40','Mariz','12345678911')

rene.set_cpf('98765432112')
novo_nome = input('digite a mudança de nome')
rene.set_nome(novo_nome)

print(rene.get_cpf())
print(rene.get_nome())

#ACESSO DIRETO A ATRIBUTOS DA CLASSE
class Trabalhador:
    #atributo da classe
    ch_max = 44

    #construtor
    def __init__(self, nct, ch, nome):
        self.nct = nct
        self.ch = ch
        self.nome = nome


rene = Trabalhador('1231234','40','rene de sousa')
print(rene.nome)
rene.ch_max = 35
rene.nome = 'rene de sousa junior'

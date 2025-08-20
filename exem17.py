#criação da classe
class Aluno:
    #cosntrutor da classe: instanciar os objetos
    def __init__(self, nome, serie, cra):

        #atributos da classe
        self.nome_aluno = nome
        if serie in [1,2,3]:
            self.serie_letiva = serie
        else:
            print('voce nao é do integrado')
            self.serie_letiva = 0

        if cra >= 0 and cra <= 100:
            self.cra = cra
        else:
            print('voce errou a nota')
            self.cra = 0

    def atribuir_media(self,media):
        self.cra = media



turma_2ano = []

for i in range(7):
    nome = input('digite o nome')
    turma_2ano.append()
#para completar: instanciar o objeto e colocar dentro da lista

#fazer outro for para calcular a media da turma


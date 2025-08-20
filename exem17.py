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

    def get_cra(self):
        return self.cra


turma_2ano = []

for i in range(7):
    nome = input('digite o nome')
    a = int(input('digite a serie'))
    asdad = float(input('digite o cra'))

    novo_aluno = Aluno(nome, a, asdad)
    turma_2ano.append(novo_aluno)

somaCRA = 0
for i in range(7):
    somaCRA = somaCRA + turma_2ano[i].get_cra()
    #somaCRA += turma_2ano[i].cra


media = somaCRA / 7
print(f'a turma do segundo ano possui media no CRA de {media}')











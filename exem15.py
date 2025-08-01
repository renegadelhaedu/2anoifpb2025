#criando uma classe
class Festa:
    def __init__(self,local,ingresso):
        self.local = None
        self.ingresso = None
        self.bandas = None

#instanciando um objeto
festa1 = Festa('Sousa',200)

bandas_tops = []
for i in range(1,5):
    nome_banda = input(f'digite o nome da banda numero {i} ')
    bandas_tops.append(nome_banda)

festa1.bandas = bandas_tops

print(festa1.bandas)



class Pet:
    def __init__(self, nome, tutor):
        self.nome = nome
        self.tutor = tutor
        self.vacinas = []

    def registar_vacina(self, nome_vacina, data):
        self.vacinas.append([nome_vacina, data])


animais = []

cachorro1 = Pet('rute', 'ana flavia')
gata1 = Pet('bobinha', 'gustavo')
papag1 = Pet('jotinha', 'junior')

animais.append(cachorro1)
animais.append(gata1)
animais.append(papag1)

nome_pet = input('qual o nome do animal que vc deseja remover da lista')
for i in range(len(animais)):
    if nome_pet == animais[i].nome:
        animais.pop(i)
        print('Animal removido do cadastro')
        break
#------------OU -----------------------------
indice = -1
for i in range(len(animais)):
    if nome_pet == animais[i].nome:
        indice = i

if indice >= 0:
    animais.pop(indice)
    print('animal retirado do cadatro')
else:
    print('nao encontramos este animal no cadastro')








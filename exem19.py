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

for bicho in animais:
    print(f'o tutor de {bicho.nome} é {bicho.tutor}')


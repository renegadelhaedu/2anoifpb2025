class Empresa:

    def __init__(self,cnpj, nome):
        self.__cnpj = cnpj
        self.__nome = nome
        self.__trabalhadores = []


    @property
    def trabalhadores(self):
        return self.__trabalhadores

    @trabalhadores.setter
    def trabalhadores(self, lista):
        self.__trabalhadores = lista

    def contratar_trabalhador(self, trabalhador):
        self.__trabalhadores.append(trabalhador)
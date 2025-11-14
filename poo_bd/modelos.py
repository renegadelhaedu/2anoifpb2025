class Entidade: #classe pai
    def __init__(self, id):
        self.__id = id

    @property
    def id(self):
        return self.__id


class Pessoa(Entidade): #classe filho
    def __init__(self, id, nome, idade):
        super().__init__(id)
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        self._idade = valor
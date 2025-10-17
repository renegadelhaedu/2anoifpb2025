from modelos.pessoa import Pessoa

class Terceirizado(Pessoa):
    def __init__(self, nome, login, senha, salario, num_clt):
        super().__init__(nome, login, senha)
        self.salario = salario
        self.num_clt = num_clt

    def almocar(self):
        print('vou para a cozinha do ifpb almoçar')



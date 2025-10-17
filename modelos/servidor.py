from modelos.pessoa import Pessoa
from utilidades.login import oi

class Servidor(Pessoa):
    def __init__(self, nome, login, senha, salario):
        super().__init__(nome, login, senha)
        self.salario = salario


    def bater_ponto(self):
        print('estou registrando meu ponto')

    def almocar(self):
        print('preciso sair para almoçar ou pedir delivery')


#instanciando um objeto da classe Servidor
reginaldo = Servidor('reginaldo','regis','123', 5000)

reginaldo.senha = '23lj1kl23j12'

reginaldo.mostrar_credencial()

reginaldo.bater_ponto()

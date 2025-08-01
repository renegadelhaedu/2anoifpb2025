#criar uma classe e instanciar um objeto desta classe
#init é o método padrao de criação de objetos, instanciador
#init é o construtor de objetos

class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.status = 'solteiro'


#instanciando um objeto da classe Pessoa
caio = Pessoa('caio jose', '23467573454')

print('o nome da pessoa é', caio.nome)
print('essa pessoa está', caio.status)
caio.status = input('digite seu estado de relacionamento ')
print('essa pessoa está', caio.status)
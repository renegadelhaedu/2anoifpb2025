from modelos.trabalhador import Trabalhador
from modelos.empresa import Empresa

isis = Empresa('234642342','laticinio belo vale')

for i in range(3):
    nome = input('digite seu nome')
    cpf = input('digite seu cpf')
    ch = input('digite sua carga horaria')
    nct = input('digite o num da CT')

    novo_tr = Trabalhador(nct,ch, nome, cpf)
    isis.contratar_trabalhador(novo_tr)


for tr in isis.trabalhadores:
    print(tr.nome)
    print(tr.cpf)

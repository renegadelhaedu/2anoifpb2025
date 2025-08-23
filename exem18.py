'''
-criar uma classe Passageiro e criar um construtor para a classe
-criar atributos da classes (nome, cpf, poltrona)
-fora da classe deve-se criar um menu para:
.cadastrar passageiro
.listar passageiros
.buscar passageiro pelo cpf


Use uma lista para armazenar os passageiros

-modifique o código para aceitar cpf com apenas 11 caracteres
-adicione um método na classe passageiro para retornar o seguinte texto:
 'meu nome é ? e eu estou sentado na poltrona ?'

'''
class Passageiro:
    def __init__(self, nome, cpf, poltrona):
        self.nome_pa = nome
        self.cpf_pa = cpf
        self.poltrona_pa = poltrona

    def verificar_vogal(self):
        if 'u' in self.nome_pa:
            return 'tem a letra u no nome '
        elif 'a' in self.nome_pa:
            return 'tem a letra a no nome '
        elif 'e' in self.nome_pa:
            return 'tem a letra e no nome '
        elif 'i' in self.nome_pa:
            return 'tem a letra i no nome '
        elif 'o' in self.nome_pa:
            return 'tem a letra o no nome '
        else:
            return 'voce nao possui vogais no nome '



lista = []

op = 47

while op != 0:
    print('--- ---')
    print('1-cadastrar ')
    print('2-listar ')
    print('3-buscar ')
    print('4-verificar vogais ')
    op = int(input('digite a opcao desejada'))

    if op == 1:
        nomepessoa = input('digite seu nome')
        cpf = int(input('digite seu cpf'))
        poltrona = int(input('qual sua poltrana'))

        novo_passageiro = Passageiro(nomepessoa, cpf, poltrona)
        lista.append(novo_passageiro)
        print('passageiro cadastrado com sucesso!')

    elif op == 2:
        #for i in range(len(lista)):
        #    print(lista[i].nome_pa)

        for passageiro in lista:
            print(passageiro.nome_pa)

    elif op == 3:
        cpf_buscado = int(input('digite o cpf para busca'))
        for passag in lista:
           if cpf_buscado == passag.cpf_pa:
               print('usuario encontrado')
               print('o nome dele é', passag.nome_pa)

    elif op == 4:
        for passag in lista:
            print(passag.verificar_vogal())

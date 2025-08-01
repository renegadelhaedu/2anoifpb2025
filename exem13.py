#desenvolva um algoritmo em python que crie uma função para contar
#quantas vogais possuem na frase recebida como entrada. a quantidade
#de vogais deve ser retornada pela função
#defina a função e chame ela com uma frase de sua preferência

def contador_vogais(frase):
    cont = 0
    for l in frase:
        if l.lower() in ['a','e','i','o','u']:
            cont += 1
    return cont

contador_vogais('eu estou com saudade de meu amigo david')
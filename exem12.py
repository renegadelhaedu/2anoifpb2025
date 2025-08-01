#recursividade infinita (erro)
def meu_dia(diario):
    print(diario)
    meu_dia(diario)

meu_dia('eu estudei')
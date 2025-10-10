arq = open('exemplo.txt','a')

for i in range(3):
    texto = input('digite algo: ')
    arq.write('\n' + texto)

arq.close()
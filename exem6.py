cand1 = 0
cand2 = 0

op = 99

while op != 0:
    voto = int(input('Vote 1 para Milena, vote 2 para Junior e 0 para encerrar'))
    if voto == 1:
        cand1 += 1
    elif voto == 2:
        cand2 += 1
    elif voto == 0:
        break

if cand1 > cand2:
    print('o candidato eleito foi o 1')
elif cand2 > cand1:
    print('o candidato eleito foi o 2')
else:
    print('vai ter segundo turno pois deu empate')

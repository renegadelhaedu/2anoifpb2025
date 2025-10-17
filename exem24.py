from modelos.meus_modelos import *

op = int(input('digite 1 para tercei ou 2 para efetivo'))

if op == 1:
    novo_ter = Terceirizado('Adilson','adiifpb','123',5000,'234953754834')
    novo_ter.almocar()
elif op == 2:
    novo_servidor = Servidor('Fatima','fatinha','123',5555)
    novo_servidor.almocar()


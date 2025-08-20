class Time:
    def __init__(self, nome_time, estado, estadio):
        self.nome = nome_time
        if estado in ['paraiba', 'ceara','piaui','maranhao','rio grande do norte']:
            self.estado = estado
        else:
            self.estado = None

        self.nome_estadio = estadio

nome = input('digite o nome do time de futebol ')
estado_time = input('de qual estado é? ')
estadio_futebol = input('qual o nome do estadio deste time? ')

sousa = Time(nome, estado_time, estadio_futebol)
print(sousa.estado)




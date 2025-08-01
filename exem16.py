class Time:
    def __init__(self, nome_time, estado, estadio):
        self.nome = nome_time
        if estado in ['paraiba', 'ceara','piaui','maranhao','rio grande do norte']:
            self.estado = estado
        else:
            self.estado = None

        self.nome_estadio = estadio

sousa = Time('sousa es club', 'paraiba','marizao')

sousa.estado = 'pernambuco'

print(sousa.estado)


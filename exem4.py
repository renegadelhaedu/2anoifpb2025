soma = 0
for i in range(4):
    idade = int(input('digite sua idade'))
    if idade > 14:
        soma = soma + idade

media = soma / 4

print(f'a idade media desta turma é {media}')
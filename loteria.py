# Código de simulação de loteria

import random

sor1 = random.randint(1,60)
sor2 = random.randint(1,60)
sor3 = random.randint(1,60)
sor4 = random.randint(1,60)
sor5 = random.randint(1,60)
sor6 = random.randint(1,60)

## Erro no sorteio (número repetido)

if (sor1 == sor2) or (sor1 == sor3) or (sor1 == sor4) or (sor1 == sor5) or (sor1 == sor6) or (sor2 == sor3) or (sor2 == sor4) or (sor2 == sor5) or (sor2 == sor6) or (sor3 == sor4) or (sor3 == sor5) or (sor3 == sor5) or (sor3 == sor6) or (sor4 == sor5) or (sor4 == sor6) or (sor5 == sor6):
    sorteados = 'erro1'
while sorteados == 'erro1':
    sor1 = random.randint(1, 60)
    sor2 = random.randint(1, 60)
    sor3 = random.randint(1, 60)
    sor4 = random.randint(1, 60)
    sor5 = random.randint(1, 60)
    sor6 = random.randint(1, 60)
    if (sor1 == sor2) or (sor1 == sor3) or (sor1 == sor4) or (sor1 == sor5) or (sor1 == sor6) or (sor2 == sor3) or (sor2 == sor4) or (sor2 == sor5) or (sor2 == sor6) or (sor3 == sor4) or (sor3 == sor5) or (sor3 == sor5) or (sor3 == sor6) or (sor4 == sor5) or (sor4 == sor6) or (sor5 == sor6):
        sorteados = 'erro1'

## Fim do erro no sorteio
    else:
        sorteados = [sor1, sor2, sor3, sor4, sor5, sor6]

## Números do jogo
jog1 = int(input('Qual o primeiro número? '))
jog2 = int(input('Qual o segundo número? '))
jog3 = int(input('Qual o terceiro número? '))
jog4 = int(input('Qual o quarto número? '))
jog5 = int(input('Qual o quinto número? '))
jog6 = int(input('Qual o sexto número? '))

## Erros no jogo (número repetido, não inteiro, ou fora do intervalo)

if jog1 > 60 or jog1 < 1:
    print('erro no primeiro número!')
    jog1 = int(input('Qual o primeiro número? '))
if jog2 > 60 or jog2 < 1:
    print('erro no segundo número!')
    jog2 = int(input('Qual o segundo número? '))
if jog3 > 60 or jog3 < 1:
    print('erro no terceiro número!')
    jog3 = int(input('Qual o terceiro número? '))
if jog4 > 60 or jog4 < 1:
    print('erro no quarto número!')
    jog4 = int(input('Qual o quarto número? '))
if jog5 > 60 or jog5 < 1:
    print('erro no quinto número!')
    jog5 = int(input('Qual o quinto número? '))
if jog6 > 60 or jog6 < 1:
    print('erro no sexto número!')
    jog6 = int(input('Qual o sexto número? '))

## fim de erros no jogo
else:
    jogo = [jog1, jog2, jog3, jog4, jog5, jog6]

## Resultado

print('os seu jogo foi:', jogo)
print('os números sorteados foram: ', sorteados)

if jogo == sorteados:
    print('Você venceu! Parabéns!')
else:
    print('Não foi dessa vez... uma pena!')
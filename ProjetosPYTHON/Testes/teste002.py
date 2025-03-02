import random

numbR = random.randint(1, 10)
tent = 0
print('Bem vindo ao jogo de adivinhar! voce tem 5 vidas! boa sorte!')

while True:
    tentA = int(input('Tente acertar o valor! >> '))
    if tentA == numbR:
        print(f'Parabens você acertou o valor que era {numbR}')
        tent += 10
        break
    elif tentA != numbR:
        print('Você erro! tente novamente')
        tent += 1
    if tentA > numbR:
        print('O valor é maior que o valor random')
    elif tentA < numbR:
        print('O valor é menor que o valor random')
    if tent == 5:
        print(f'Você perdeu todas as suas vida! o valor era {numbR}')
        break

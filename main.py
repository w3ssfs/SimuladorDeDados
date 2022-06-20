import random
from time import sleep



def linha ():
    print("="*30)


def dado ():

    dados = random.randint(1,6)
    while True:
        try:
            respo = input('Quer Jogar um Dado? \n>> ')
            if respo == 'sim' or respo == 's':
                print(f'Dados Girando.........')
                sleep(1)
                print(f'Número: {dados}')
                break
            elif respo == 'nao' or respo == 'n':
                print('Obrigado, Volte sempre para jogar XD')
                break
            else:
                print('Por favor digite Sim ou Nao')
                linha()
        except:
            print('ERRO! Responda com SIM ou NAO!')

linha()
print(f'\033[1;32m{"Simulador de Dados":^30}\033[m')
linha()
dado()
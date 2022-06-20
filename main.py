import random
from time import sleep
import PySimpleGUI as sg


def linha ():
    print("="*30)









def dado ():
    # Layout
    layout = [
        [sg.Text('Jogar Dado?')],
        [sg.Button('sim'), sg.Button('nao')]
    ]

    # criar uma janela
    janela = sg.Window('Simulador de Dado', layout=layout)
    # Ler os valores
    evento, valores = janela.Read()
    # Fazer alguma coisa


    dados = random.randint(1,6)
    while True:
        try:

                if evento == 'sim' or evento == 's':
                    print(f'Dados Girando.........')
                    sleep(1)
                    print(f'Número: {dados}')
                    break
                elif evento == 'nao' or evento == 'n':
                    print('Obrigado, Volte sempre para jogar XD')
                    break
                else:
                    print('Por favor digite Sim ou Nao')
                    linha()
                    break
        except:
                print('ERRO! Responda com SIM ou NAO!')

linha()
print(f'\033[1;32m{"Simulador de Dados":^30}\033[m')
linha()
dado()
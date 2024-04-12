from winsound import PlaySound
from winsound import SND_ASYNC
import time
import keyboard

special_keys = [
    ['space', r'assests\space.wav'],
    ['backspace', r'assests\backspace.wav'],
    ['enter', r'assests\enter.wav']
    ]

default_sounds = [
    r'assests\tec1.wav',
    r'assests\tec2.wav',
    r'assests\tec3.wav',
    r'assests\tec4.wav'
    ]

choices = [
    'mudar o som',
    'mudar menu',
    'sair do menu',
    'fechar app',
    'ms',
    'mm',
    'sm',
    'q'
    ]

shortcuts = ['ms', 'mm', 'sm', 'q']

def getSound():
    '''Pergunta qual som o usuário quer escolher para as teclas'''
    try:
        som = int(input('Qual som a tecla deve fazer: '))
    except:
        som = -1

    while not 0 <= som <= 3:
        try:
            som = int(input('Tem que ser um numero inteiro de 0 a 3! '))
        except:
            pass
    print('Som definido para o '+ str(som))
    return som



def getMenuKey():
    '''Lê a tecla que será o menu, e a retorna'''
    menu = keyboard.read_key()
    print('A tecla "'+menu+'" foi defina como menu')
    return menu



def main():
    isRunning = True
    menu = 'esc'
    print('Você tem 4 opções de sons, enumeradas de 0 - 3')
    time.sleep(2)
    print('Escolha uma delas e veja se gostou')
    time.sleep(2)
    print('Se quiser trocar, use o menu, que por padrão está na tecla "esc"')
    time.sleep(2)
    som = getSound()

    while isRunning:
        event = keyboard.read_event()
        normal_key = True
        if event.event_type == 'down':
            '''verifica se o tipo do input é 'down' para evitar repetição de som'''
            
            for i in range(3):
                if event.name == special_keys[i][0]:
                    '''verifica se a tecla é especial'''
                    
                    PlaySound(special_keys[i][1], SND_ASYNC)
                    normal_key = False
        
            if normal_key and len(event.name) == 1:
                '''verifica se alguma tecla especial foi pressionada antes de tocar o som default'''
                
                PlaySound(default_sounds[som], SND_ASYNC)

            if event.name == menu:
                print('')
                print('O que quer fazer? ')
                time.sleep(1)
                print('Você tem essas opcões:')
                time.sleep(1)
                print('')
                print('========================')
                print('')
                print(*choices[:4], sep='\n')
                print('')
                print('========================')
                print('')
                choice = input('Qual você vai escolher? ').strip().lower()
                while not choice in choices:
                    print('')
                    print('Essa opcão não existe')
                    time.sleep(0.5)
                    choice = input('Qual você vai escolher? ').strip().lower()

                if choice == choices[0] or choice == 'ms':
                    som = getSound()

                elif choice == choices[1] or choice == 'mm':
                    print('Redefina a tecla de menu: ')
                    time.sleep(1)
                    menu = getMenuKey()
                    time.sleep(1)

                elif choice == choices[2] or choice == 'sm':
                    pass

                elif choice == choices[3] or choice == 'q':
                    isRunning = False
                
        else:
            pass



if __name__ == '__main__':
    main()

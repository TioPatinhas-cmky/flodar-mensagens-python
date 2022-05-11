from pyautogui import alert, hotkey
from pyperclip import copy
from time import sleep

q_m = int(input('Quantas Mensagens deseja enviar? ')) #q_m (quantidade mensagem)
mensagem = str(input('Qual é a Mensagem a ser enviada? '))

alert('Clique no campo onde a mensagem será escrita em seguida, ok. Não aperte em nada depois disso')

for c in range(0, q_m +1):
    sleep(0)
    copy(mensagem)
    sleep(0)
    hotkey('ctrl', 'v')
    sleep(0)
    hotkey('Enter')
    sleep(0)
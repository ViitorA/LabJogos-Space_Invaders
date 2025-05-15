from PPlay.window import *
from PPlay.sprite import *

import config
import states.menu as menu
import states.jogo as jogo
import states.dificuldades as dificuldades
import states.ranking as ranking

def init():
    # JANELA
    config.janela = Window(1200,600)
    config.janela.set_title("Victor Alexander")

    # TECLADO
    config.teclado = config.janela.get_keyboard()

    # MOUSE
    config.mouse = config.janela.get_mouse()
    config.ultimo_clique = 0
        
init()

# O controlador controla(kk) o estado atual do jogo(em que cenário/janela ele se encontra)
# incializa ele no menu pois é a primeira tela que deve aparecer ao abrir o jogo
config.CONTROLADOR = config.MENU

# ---| LOOP PRINCIPAL |---
while True:
    match config.CONTROLADOR:
        case config.MENU:
            menu.abrir_menu()
        case config.JOGO:
            jogo.iniciar_jogo()
        case config.DIFICULDADES:
            dificuldades.mostrar_dificuldades()
        case config.RANKING:
            ranking.mostrar_ranking()

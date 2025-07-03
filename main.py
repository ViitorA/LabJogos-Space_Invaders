# O código funcionava normalmente, porém visto que não era modularizado e estava todo o código num mesmo arquivo, quase todo o código 
# anterior teve de ser modificado ou removido p/a a modularização.

# Criei o módulo config.py para algumas variáveis globais que são usadas em todo projeto
# Criei os módulos menu.py e jogo.py para as "telas" do jogo
# Criei os módulos player.py e inimigos.py para maior legibilidade e manipulação de dados
# Criei o módulo utils.py para algumas funções úteis

from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.mouse import *

import pygame

import config
from states.jogo import jogo
from states.menu import menu
from states.dificuldades import mostrar_dificuldades
from states.dificuldades import alterar_dificuldade
from states.ranking import mostrar_ranking

def init():
    # Janela e controle
    config.janela = Window(800, 600)
    config.janela.set_title("SPACE INVADERS")

    config.teclado = Window.get_keyboard()
    config.mouse = Window.get_mouse()
    config.ultimo_clique = pygame.time.get_ticks()

    config.estado = "menu"
    
    alterar_dificuldade(1) # Coloca a dificuldade em fácil

init()

# Loop principal
while True:
    if config.estado == "menu":
        menu()
    elif config.estado == "jogo":
        jogo()
    elif config.estado == "dificuldades":
        mostrar_dificuldades()
    elif config.estado == "ranking":
        mostrar_ranking()

    config.janela.update()

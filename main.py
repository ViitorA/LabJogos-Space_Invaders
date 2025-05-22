from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.mouse import *

import pygame

import config
from jogo import jogo
from menu import menu
from dificuldades import mostrar_dificuldades
from dificuldades import alterar_dificuldade

def carregar_sprites():
    sprites = {
        "botao_jogar": Sprite("assets/jogar.png"),
        "botao_dificuldades": Sprite("assets/dificuldade.png"),
        "botao_ranking": Sprite("assets/ranking.png"),
        "botao_sair": Sprite("assets/sair.png"),

        "botao_facil": Sprite("assets/facil.png"),
        "botao_medio": Sprite("assets/medio.png"),
        "botao_dificil": Sprite("assets/dificil.png"),

        "player": Sprite("assets/nave.png"),
        "tiro-jogador": Sprite("assets/tiro-jogador.png"),

        "inimigo": Sprite("assets/inimigo.png")
    }

    return sprites

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

# Carrega os recursos do jogo
sprites = carregar_sprites()

# Loop principal
while True:
    if config.estado == "menu":
        menu(sprites)
    elif config.estado == "dificuldades":
        mostrar_dificuldades(sprites)

    elif config.estado == "jogo":
        jogo(sprites)
            
    config.janela.update()

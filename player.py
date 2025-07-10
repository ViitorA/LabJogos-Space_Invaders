from PPlay.sprite import *

import config
import states.dificuldades

global sprite

# Velocidade padrão é fácil
velocidade = states.dificuldades.VELOCIDADE_FACIL

global vida
pontos = 0000

respawnou = False
ignore_colision = False
tempo_desde_respawn = 0
respawn_cooldown = 2


def init():
    global sprite
    global vida

    sprite = Sprite("assets/nave.png")
    vida = 3

def center():
    """CENTRALIZA O SPRITE DO PLAYER"""
    global sprite
    sprite.set_position( (config.janela.width-sprite.width)/2, config.janela.height - sprite.height-20)

def movement_processing(delta_t):
    global sprite
    global velocidade
    
    if config.teclado.key_pressed("A") and sprite.x > 0:
        sprite.x -= velocidade * delta_t
    elif config.teclado.key_pressed("D") and sprite.x + sprite.width < config.janela.width:
        sprite.x += velocidade * delta_t



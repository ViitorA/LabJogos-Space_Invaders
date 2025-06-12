from PPlay.sprite import *

import config

global sprite
velocidade = 200

global vida

respawnou = False
tempo_desde_respawn = 0
respawn_cooldown = 2

ignore_colision = False

def init():
    global sprite
    global vida

    sprite = Sprite("assets/nave.png")
    vida = 3

def movement_processing(delta_t):
    global sprite
    global velocidade
    
    if config.teclado.key_pressed("A") and sprite.x > 0:
        sprite.x -= velocidade * delta_t
    elif config.teclado.key_pressed("D") and sprite.x + sprite.width < config.janela.width:
        sprite.x += velocidade * delta_t



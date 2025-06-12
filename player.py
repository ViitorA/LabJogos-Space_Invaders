from PPlay.sprite import *

import config

global sprite
velocidade = 200

def init():
    global sprite
    sprite = Sprite("assets/nave.png")

def movement_processing(delta_t):
    global sprite
    global velocidade
    
    if config.teclado.key_pressed("A") and sprite.x > 0:
        sprite.x -= velocidade * delta_t
    elif config.teclado.key_pressed("D") and sprite.x + sprite.width < config.janela.width:
        sprite.x += velocidade * delta_t



import pygame

import config

def clicou(botao):
    tempo_atual = pygame.time.get_ticks()
    
    clicou = config.mouse.is_over_object(botao) and config.mouse.is_button_pressed(1) and tempo_atual - config.ultimo_clique > config.delay_entre_cliques
    
    if clicou:
        config.ultimo_clique = pygame.time.get_ticks()

    return clicou

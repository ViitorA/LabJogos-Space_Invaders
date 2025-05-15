from PPlay.sprite import *

import config

def mostrar_dificuldades():
    while True:
        # VISUAL
        config.janela.set_background_color([15,0,25])

        # tamanho sprites: 200x120
        botao_facil = Sprite("assets/facil.png", frames = 1)
        botao_facil.set_position( (config.janela.width-botao_facil.width)/2, 40)

        botao_medio = Sprite("assets/medio.png", frames = 1)
        botao_medio.set_position( (config.janela.width-botao_medio.width)/2, 80+120)

        botao_dificil = Sprite("assets/dificil.png", frames = 1)
        botao_dificil.set_position( (config.janela.width-botao_dificil.width)/2, 120+240)

        botao_facil.draw()
        botao_medio.draw()
        botao_dificil.draw()

        config.janela.update()

        # LÓGICA
        tempo_atual = pygame.time.get_ticks()
        
        if config.teclado.key_pressed("ESC"):
            config.CONTROLADOR = config.MENU
            return 0

        # Caso não entenda o ultimo 'and' verifique o config.py
        if config.mouse.is_button_pressed(1) and config.mouse.is_over_object(botao_facil) and tempo_atual - config.ultimo_clique > config.delay_entre_cliques:
            config.dificuldade = 1
            
            config.CONTROLADOR = config.JOGO
            return 0
            
        if config.mouse.is_button_pressed(1) and config.mouse.is_over_object(botao_medio) and tempo_atual - config.ultimo_clique > config.delay_entre_cliques:
            config.dificuldade = 2

            config.CONTROLADOR = config.JOGO
            return 0

        if config.mouse.is_button_pressed(1) and config.mouse.is_over_object(botao_dificil) and tempo_atual - config.ultimo_clique > config.delay_entre_cliques:
            config.dificuldade = 3

            config.CONTROLADOR = config.JOGO
            return 0

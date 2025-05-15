from PPlay.sprite import *

import config

def abrir_menu():
    while True: 
        # VISUAL
        config.janela.set_background_color([15,0,25])
       
        # tamanho sprites: 200x120
        # TODO: tornar esses números de altura mais legíveis
        botao_jogar = Sprite("assets/jogar.png", frames = 1)
        botao_jogar.set_position( (config.janela.width-botao_jogar.width)/2, 20)
        
        botao_dificuldade = Sprite("assets/dificuldade.png", frames = 1)
        botao_dificuldade.set_position( (config.janela.width-botao_dificuldade.width)/2, 40+120)

        botao_ranking = Sprite("assets/ranking.png", frames = 1)
        botao_ranking.set_position( (config.janela.width-botao_ranking.width)/2, 60+240)

        botao_sair = Sprite("assets/sair.png", frames = 1)
        botao_sair.set_position( (config.janela.width-botao_sair.width)/2, 80+360)

        botao_jogar.draw()
        botao_dificuldade.draw()
        botao_ranking.draw()
        botao_sair.draw()

        config.janela.update()
        
        # LÓGICA
        tempo_atual = pygame.time.get_ticks()
        
        # Caso não entenda o último 'and' verifique o config.py
        if config.mouse.is_button_pressed(1) and config.mouse.is_over_object(botao_jogar) and tempo_atual - config.ultimo_clique > config.delay_entre_cliques:
            config.ultimo_clique = pygame.time.get_ticks()

            config.CONTROLADOR = config.JOGO
            return 0
        
        if config.mouse.is_button_pressed(1) and config.mouse.is_over_object(botao_dificuldade) and tempo_atual - config.ultimo_clique > config.delay_entre_cliques:
            config.ultimo_clique = pygame.time.get_ticks()

            config.CONTROLADOR = config.DIFICULDADES
            return 0

        if config.mouse.is_button_pressed(1) and config.mouse.is_over_object(botao_ranking) and tempo_atual - config.ultimo_clique > config.delay_entre_cliques:
            config.ultimo_clique = pygame.time.get_ticks()

            config.CONTROLADOR = config.RANKING
            return 0

        if config.mouse.is_button_pressed(1) and config.mouse.is_over_object(botao_sair) and tempo_atual - config.ultimo_clique > config.delay_entre_cliques:
            config.janela.close()


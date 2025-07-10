import pygame

import config
import player
import states.game_over as game_over

def clicou(botao):
    tempo_atual = pygame.time.get_ticks()
    
    clicou = config.mouse.is_over_object(botao) and config.mouse.is_button_pressed(1) and tempo_atual - config.ultimo_clique > config.delay_entre_cliques
    
    if clicou:
        config.ultimo_clique = pygame.time.get_ticks()

    return clicou

def detector_colisoes(lista_tiros, lista_inimigos):
    tiros_para_remover = []
    inimigos_para_remover = []

    verificar_colisao = True

    for tiro in lista_tiros:
        if tiro["owner"] == "jogador":
            for inimigo in lista_inimigos:
                # TODO
                #if inimigo["pos_mat_x"] == 0 and inimigo["sprite"].x > tiro["sprite"].x + tiro["sprite"].width:
                #    verificar_colisao = False
                
                if tiro["sprite"].collided_perfect(inimigo["sprite"]):
                    tiros_para_remover.append(tiro)
                    inimigos_para_remover.append(inimigo)
                    player.pontos += 10
                    
                    # Quando um inimigo é morto, o inimigo atrás dele agora pode atirar
                    col = inimigo["pos_mat_x"]
                    row = inimigo["pos_mat_y"]
                    inimigo_atras = next( 
                        (i for i in lista_inimigos if i["pos_mat_x"] == col and i["pos_mat_y"] == row - 1),
                        None
                    )
                    if inimigo_atras:
                        inimigo_atras["frontal"] = True
                    break  # Um tiro só pode acertar um inimigo
        else: # Se o tiro for do inimigo
            # Verifica a posição do tiro e se vale a pena verificar se ele colidiu ou não
            if tiro["sprite"].x + tiro["sprite"].width < player.sprite.x:
                verificar_colisao = False
            elif tiro["sprite"].x > player.sprite.x + player.sprite.width:
                verificar_colisao = False
            elif tiro["sprite"].y + tiro["sprite"].height < player.sprite.y:
                verificar_colisao = False
            elif tiro["sprite"].y > player.sprite.y + player.sprite.height:
                verificar_colisao = False

            if verificar_colisao and not player.ignore_colision and tiro["sprite"].collided_perfect(player.sprite):
                tiros_para_remover.append(tiro)
                player.vida -= 1
                if player.vida == 0:
                    game_over.show()
                else:
                    player.respawnou = True
                    player.center()

        if tiro["sprite"].y + tiro["sprite"].height < 0 or tiro["sprite"].y > config.janela.height:
            tiros_para_remover.append(tiro)

    for tiro in tiros_para_remover:
        if tiro in lista_tiros:
            lista_tiros.remove(tiro)
    
    for inimigo in inimigos_para_remover:
        if inimigo in lista_inimigos:
            lista_inimigos.remove(inimigo)
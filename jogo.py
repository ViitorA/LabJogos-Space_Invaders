import pygame
from PPlay.sprite import *

import config
from ui import mostrar_ui
import player
import inimigos

lista_inimigos = []
lista_tiros = []

jogo_comecou = False
inimigo_spawnado = False

def game_over():
    while True:
        config.janela.set_background_color([80,10,40])

        # Uso algumas funções do pygame para poder achar as dimensões do texto renderizado p/a centralizá-lo
        text_surface = pygame.font.SysFont('Tahoma', 50).render("GAME OVER", True, (255,255,255))
        text_rect = text_surface.get_rect()
        text_rect.centerx = config.janela.width // 2
        text_rect.centery = config.janela.height // 2

        config.janela.draw_text("GAME OVER", text_rect.x, text_rect.y, size = 50, color = (255,255,255), font_name = 'Tahoma', bold = True, italic = False) 
        
        config.janela.update()
    
        if config.teclado.key_pressed("ESC"):
            config.estado = "menu"

            global lista_tiros, lista_inimigos, inimigo_spawnado, jogo_comecou
            lista_tiros = []
            lista_inimigos = []
            jogo_comecou = False
            inimigo_spawnado = False
            break

def spawnar_tiro(x,y, owner):
    tiro = {
        "x": x,
        "y": y
    }

    match owner:
        case "jogador":
            tiro["owner"] = "jogador"
            tiro["sprite"] = Sprite("assets/tiro-jogador.png")
        case "inimigo":
            tiro["owner"] = "inimigo"
            tiro["sprite"] = Sprite("assets/tiro-inimigo.png")

    tiro["width"] = tiro["sprite"].width
    tiro["height"] = tiro["sprite"].height
    tiro["x1"] = tiro["x"] + tiro["width"]
    tiro["y1"] = tiro["y"] + tiro["height"]

    lista_tiros.append(tiro)

def atualizar_objetos(delta_t):
    for tiro in lista_tiros[:]:
        if tiro["y"] + tiro["height"] < 0 or tiro["y"] > config.janela.height:
            lista_tiros.remove(tiro)
            
        if tiro["owner"] == "jogador":
            tiro["y"] -= 200 * delta_t
        elif tiro["owner"] == "inimigo":
            tiro["y"] += 200 * delta_t  
        
    inimigos.move_todos(lista_inimigos, delta_t)

    for inimigo in lista_inimigos[:]:
        if inimigo["y"] + inimigo["sprite"].height >= player.sprite.y:
            game_over()

def desenhar_objetos():
    for tiro in lista_tiros:
        tiro["sprite"].set_position(tiro["x"], tiro["y"])
        tiro["sprite"].draw()

    for inimigo in lista_inimigos:
        inimigos.draw(inimigo)

def detector_colisoes():
    tiros_para_remover = []
    inimigos_para_remover = []

    # TODO: IMPLEMENTAR A OTIMIZAÇÃO DE COLISÃO QUE O PROFESSOR FALOU 
    for tiro in lista_tiros:
        if tiro["owner"] == "jogador":
            for inimigo in lista_inimigos:
                if tiro["sprite"].collided_perfect(inimigo["sprite"]):                    
# TODO: depois que o inimigo morrer, passar o true para o da linha anterior
                    tiros_para_remover.append(tiro)
                    inimigos_para_remover.append(inimigo)
                    break  # Um tiro só pode acertar um inimigo
        else: # Se o tiro for do inimigo
            if not player.ignore_colision and tiro["sprite"].collided_perfect(player.sprite):
                tiros_para_remover.append(tiro)
                player.vida -= 1
                if player.vida == 0:
                    game_over()
                else:
                    player.respawnou = True

    for tiro in tiros_para_remover:
        if tiro in lista_tiros:
            lista_tiros.remove(tiro)
    
    for inimigo in inimigos_para_remover:
        if inimigo in lista_inimigos:
            lista_inimigos.remove(inimigo)


def jogo():
    global jogo_comecou, inimigo_spawnado, ultimo_tiro

    delta_t = config.janela.delta_time()
    tempo_atual = pygame.time.get_ticks()

    config.janela.set_background_color([20,10,40])

    if not jogo_comecou:
        player.init()
        player.sprite.set_position( (config.janela.width-player.sprite.width)/2, config.janela.height - player.sprite.height-20)
        ultimo_tiro = 0.0

        jogo_comecou = True

    if not inimigo_spawnado:
        inimigos.spawn(10, 10, 4, 3)
        inimigo_spawnado = True
    
    if config.teclado.key_pressed("ESC"):
        config.estado = "menu"


    if player.respawnou:
        player.ignore_colision = True
        player.tempo_desde_respawn += delta_t
        if int(player.tempo_desde_respawn) > player.respawn_cooldown:
            player.respawnou = False
            player.ignore_colision = False
            player.tempo_desde_respawn = 0
        else:
            if int((player.tempo_desde_respawn // 0.5) % 2) == 0:
                player.sprite.hide()
            else:
                player.sprite.unhide()
            
    player.movement_processing(delta_t)

    # Ao apertar a barra de espaço o jogador atira
    if config.teclado.key_pressed("SPACE") and tempo_atual - ultimo_tiro > config.tempo_recarga:
        spawnar_tiro(player.sprite.x + player.sprite.width/2, player.sprite.y - 10, "jogador")
        ultimo_tiro = pygame.time.get_ticks()
    
    if (tempo_atual - inimigos.ultimo_tiro) > inimigos.cooldown:
        inimigos.atirar(3)
        inimigos.ultimo_tiro = pygame.time.get_ticks()

    atualizar_objetos(delta_t)
    desenhar_objetos()
    detector_colisoes()
    mostrar_ui()

    player.sprite.draw()

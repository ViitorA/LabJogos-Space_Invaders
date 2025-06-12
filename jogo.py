import pygame
from PPlay.sprite import *

import config
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

            global lista_tiros, lista_inimigos, inimigo_spawnado
            lista_tiros = []
            lista_inimigos = []
            inimigo_spawnado = False
            break

def spawnar_tiro(x,y, owner):
    tiro = {
        "sprite": Sprite("assets/tiro-jogador.png"),
        "x": x,
        "y": y
    }

    tiro["width"] = tiro["sprite"].width
    tiro["height"] = tiro["sprite"].height
    tiro["x1"] = tiro["x"] + tiro["width"]

    match owner:
        case "jogador":
            tiro["owner"] = "jogador"
        case "inimigo":
            tiro["owner"] = "inimigo"

    lista_tiros.append(tiro)

def atualizar_objetos(delta_t):
    for tiro in lista_tiros:
        if tiro["y"] + tiro["height"] < 0 :
            lista_tiros.remove(tiro)
            
        if tiro["owner"] == "jogador":
            tiro["y"] -= 200 * delta_t
        elif tiro["owner"] == "inimigo":
            tiro["y"] += 200 * delta_t  
        
    for inimigo in lista_inimigos:
        inimigos.move(inimigo, delta_t)

        if inimigo["y1"] >= player.sprite.y:
            game_over()

def desenhar_objetos():
    for tiro in lista_tiros:
        tiro["sprite"].set_position(tiro["x"], tiro["y"])
        tiro["sprite"].draw()

    for inimigo in lista_inimigos:
        inimigos.draw(inimigo)

def detector_colisoes():
    # TODO: Colisão tá meio bugada ainda, tem alguns monstros que desaparecem ao invés de outro

    tiros_para_remover = []
    sprites_para_remover = []

    for tiro in lista_tiros:
        for inimigo in lista_inimigos:
            if (
                tiro["y"] <= inimigo["y1"] and
                tiro["x"] <= inimigo["x1"] and
                tiro["x1"] >= inimigo["x"]
            ):
                for linha in inimigo["sprites"]:
                    for sprite in linha:
                        if tiro["sprite"].collided_perfect(sprite):
                            tiros_para_remover.append(tiro)
                            sprites_para_remover.append((linha, sprite))
                            break
                    else: # executa somente se o for do sprite in linha não foi interrompido por um break
                        continue
                    break
    
    for tiro in tiros_para_remover:
        if tiro in lista_tiros:
            lista_tiros.remove(tiro)
    
    for linha, sprite in sprites_para_remover:
        if sprite in linha:
            linha.remove(sprite)


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
    
    # Processa os inputs de movimento do jogador
    player.movement_processing(delta_t)
   
    # Ao apertar a barra de espaço o jogador atira
    if config.teclado.key_pressed("SPACE") and tempo_atual - ultimo_tiro > config.tempo_recarga:
        spawnar_tiro(player.sprite.x + player.sprite.width/2, player.sprite.y - 10, "jogador")
        ultimo_tiro = pygame.time.get_ticks()

    
    atualizar_objetos(delta_t)
    desenhar_objetos()
    detector_colisoes()
    player.sprite.draw()

import pygame
from PPlay.sprite import *

import config
import player
import inimigos

lista_objetos = []
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
            break

def spawnar_tiro(sprites, x,y, owner):
    tiro = {
        "type": "tiro",
        "x": x,
        "y": y
    }

    match owner:
        case "jogador":
            tiro["owner"] = "jogador"
            tiro["sprite"] = sprites["tiro-jogador"]
            tiro["height"] = sprites["tiro-jogador"].height
            tiro["width"] = sprites["tiro-jogador"].width
        case "inimigo":
            tiro["owner"] = "inimigo"

    lista_objetos.append(tiro)

    

def atualizar_objeto(objeto, delta_t):
    if objeto["type"] == "tiro":
        if objeto["y"] < 0 - objeto["height"]:
            lista_objetos.remove(objeto)
        
        if objeto["owner"] == "jogador":
            objeto["y"] -= 200 * delta_t
        elif objeto["owner"] == "inimigo":
            objeto["y"] += 200 * delta_t  
    elif objeto["type"] == "inimigo":
        inimigos.move(objeto, delta_t)

        if objeto["y1"] >= player.sprite.y:
            game_over()

def desenhar_objeto(objeto):
    if objeto["type"] == "inimigo":
        inimigos.draw(objeto)
    else:
        objeto["sprite"].set_position(objeto["x"], objeto["y"])
        objeto["sprite"].draw()

def jogo(sprites):
    delta_t = config.janela.delta_time()
    tempo_atual = pygame.time.get_ticks()

    player.init(sprites)
    
    global ultimo_tiro

    # SPAWNA INIMIGOS
    global inimigo_spawnado
    if not inimigo_spawnado:
        inimigos.spawn(sprites, 10, 10, 4, 3)
        inimigo_spawnado = True

    if not config.game_started:
        player.sprite.set_position( (config.janela.width-player.sprite.width)/2, config.janela.height - player.sprite.height-20)
        ultimo_tiro = 0.0
        config.game_started = True

    config.janela.set_background_color([20,10,40])
    
    if config.teclado.key_pressed("ESC"):
        config.estado = "menu"
    
    # Processa os inputs de movimento do jogador
    player.movement_processing(delta_t)
   
    # Ao apertar a barra de espaço o jogador atira
    if config.teclado.key_pressed("SPACE") and tempo_atual - ultimo_tiro > config.tempo_recarga:
        spawnar_tiro(sprites, player.sprite.x + player.sprite.width/2, player.sprite.y - 10, "jogador")
        ultimo_tiro = pygame.time.get_ticks()

    for objeto in lista_objetos:
        atualizar_objeto(objeto, delta_t)
        desenhar_objeto(objeto)

    player.sprite.draw()

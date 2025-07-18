import datetime
import pygame
from PPlay.sprite import *

import config
from uteis import detector_colisoes
from ui import mostrar_ui
import player
import inimigos
import states.game_over as game_over

lista_inimigos = []
lista_tiros = []

tempo_atirando = 0
mudou_de_sprite = False

wave_number = 1
wave_info = [0,0] # Armazena qtd linhas e colunas da wave atual

jogo_comecou = False
inimigo_spawnado = False

ultimo_tiro = 0.0
tempo_resfriamento = 0

def resetar_variaveis():
    global lista_tiros, lista_inimigos, wave_number, inimigo_spawnado, jogo_comecou 
    lista_tiros = []
    lista_inimigos = []
    wave_number = 1
    jogo_comecou = False
    inimigo_spawnado = False

def new_wave():
    global wave_number, lista_tiros, lista_inimigos, inimigo_spawnado, jogo_comecou, ultimo_tiro
    wave_number += 1
    lista_tiros = []
    player.center()
    ultimo_tiro = 0.0
    inimigo_spawnado = False

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
    """ATUALIZA A POSIÇÃO DOS OBJETOS"""
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
            game_over.show()

def desenhar_objetos():
    """DESENHA OS OBJETOS NA TELA"""
    for tiro in lista_tiros:
        tiro["sprite"].set_position(tiro["x"], tiro["y"])
        tiro["sprite"].draw()

    for inimigo in lista_inimigos:
        inimigos.draw(inimigo)

def jogo():
    global jogo_comecou, inimigo_spawnado, ultimo_tiro

    delta_t = config.janela.delta_time()
    tempo_atual = pygame.time.get_ticks()

    config.janela.set_background_color([20,10,40])

    if not jogo_comecou:
        player.init()
        player.center()
        ultimo_tiro = 0.0

        jogo_comecou = True

    if not inimigo_spawnado:
        enemies_lines = 4 + wave_number
        enemies_columns = 3 + wave_number
        inimigos.spawn(10, 80, enemies_lines, enemies_columns)
        wave_info[0] = enemies_lines
        wave_info[1] = enemies_columns
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

    global tempo_atirando,mudou_de_sprite, tempo_resfriamento
    # Ao apertar a barra de espaço o jogador atira
    if config.teclado.key_pressed("SPACE"):
        tempo_resfriamento = 0
        if (tempo_atual - ultimo_tiro > config.tempo_recarga):
            spawnar_tiro(player.sprite.x + player.sprite.width/2, player.sprite.y - 10, "jogador")
            ultimo_tiro = pygame.time.get_ticks()
        
        tempo_atirando += delta_t
        
        if int(tempo_atirando) >= 2 and mudou_de_sprite:
            mudou_de_sprite = False

        if int(tempo_atirando) >= 2 and not mudou_de_sprite:
            if player.sprite_atual == 0:
                player.change_sprite(1)
                mudou_de_sprite = True
                tempo_atirando = 0
            elif player.sprite_atual == 1:
                player.change_sprite(2)
                mudou_de_sprite = True
                tempo_atirando = 0
            elif player.sprite_atual == 2:
                player.vida -= 1
                if player.vida == 0:
                    game_over.show()
                else:
                    player.respawnou = True
                    player.change_sprite(0)
                    tempo_atirando = 0
                    player.center()
    else:
        tempo_resfriamento += delta_t
        tempo_atirando = 0
        
        if int(tempo_resfriamento) >= 2:
            if player.sprite_atual == 1:
                player.change_sprite(0)
                mudou_de_sprite = True
                tempo_resfriamento = 0
            elif player.sprite_atual == 2:
                player.change_sprite(1)
                mudou_de_sprite = True
                tempo_resfriamento = 0    
    print(tempo_atirando)
    print("Tempo de resfriamento: " + str(tempo_resfriamento))

    
    if (tempo_atual - inimigos.ultimo_tiro) > inimigos.cooldown:
        inimigos.atirar()
        inimigos.ultimo_tiro = pygame.time.get_ticks()

    atualizar_objetos(delta_t)
    desenhar_objetos()
    detector_colisoes(lista_tiros, lista_inimigos)
    mostrar_ui()

    if lista_inimigos == []:
        new_wave()

    player.sprite.draw()

import random

from PPlay.sprite import *
import config
import states.jogo as jogo

cooldown = 2000
ultimo_tiro = 0

def spawn(x, y, m, n):
    largura = Sprite("assets/inimigo.png").width
    altura = Sprite("assets/inimigo.png").height
    gap_x = largura // 2
    gap_y = altura // 2

    pos_mat_x = 0
    pos_mat_y = 0
    for linha in range(n):
        for coluna in range(m):
            inimigo = {
                "sprite": Sprite("assets/inimigo.png"),
                "x": x + (largura + gap_x) * coluna,
                "y": y + (altura + gap_y) * linha,
                "pos_mat_x": pos_mat_x,
                "pos_mat_y": pos_mat_y,
                "velocidade": 50
            }

            inimigo["x1"] = inimigo["x"] + inimigo["sprite"].width
            inimigo["y1"] = inimigo["y"] + inimigo["sprite"].height

            if linha == n-1:
                inimigo["frontal"] = True
            else:
                inimigo["frontal"] = False

            jogo.lista_inimigos.append(inimigo)
            pos_mat_x += 1
        pos_mat_x = 0
        pos_mat_y += 1

def move_todos(lista_inimigos, delta_t):
    # P/a ver se algum inimigo bateu na borda
    bateu = False

    for inimigo in lista_inimigos:
        novo_x = inimigo["x"] + inimigo["velocidade"] * delta_t
        if novo_x + inimigo["sprite"].width >= config.janela.width or novo_x <= 0:
            bateu = True
            break

    # Se algum bateu, todos descem e invertem velocidade
    if bateu:
        for inimigo in lista_inimigos:
            inimigo["y"] += 70
            inimigo["velocidade"] *= -1

    # Agora move todos normalmente
    for inimigo in lista_inimigos:
        inimigo["x"] += inimigo["velocidade"] * delta_t

def draw(inimigo):
    inimigo["sprite"].set_position(inimigo["x"], inimigo["y"])
    inimigo["sprite"].draw()

def atirar():
    inimigos_frontais = [inimigo for inimigo in jogo.lista_inimigos if inimigo["frontal"]]
    if inimigos_frontais:
        inimigo_escolhido = random.choice(inimigos_frontais)
        jogo.spawnar_tiro(inimigo_escolhido["sprite"].x, 
                          inimigo_escolhido["sprite"].y + inimigo_escolhido["sprite"].height, 
                          "inimigo") 

from utils import clicou
from PPlay.sprite import *
import config

def alterar_dificuldade(dificuldade):
    config.dificuldade = dificuldade

    if dificuldade == 1:
        config.velocidade_jogador = 300
        config.tempo_recarga = 200
    elif dificuldade == 2:
        config.velocidade_jogador = 220
        config.tempo_recarga = 300
    elif dificuldade == 3:
        config.velocidade_jogador = 190
        config.tempo_recarga = 400

def mostrar_dificuldades():
    botao_facil = Sprite("assets/facil.png")
    botao_facil.set_position( (config.janela.width-botao_facil.width)/2, 40)

    botao_medio = Sprite("assets/medio.png")
    botao_medio.set_position( (config.janela.width-botao_medio.width)/2, 80+120)

    botao_dificil = Sprite("assets/dificil.png")
    botao_dificil.set_position( (config.janela.width-botao_dificil.width)/2, 120+240)

    config.janela.set_background_color([0,0,15])

    botao_facil.draw()
    botao_medio.draw()
    botao_dificil.draw()

    if clicou(botao_facil):
        alterar_dificuldade(1)
        config.estado = "jogo"
    elif clicou(botao_medio):
        alterar_dificuldade(2)
        config.estado = "jogo"
    elif clicou(botao_dificil):
        alterar_dificuldade(3)
        config.estado = "jogo"


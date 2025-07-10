from PPlay.sprite import *
import config
import uteis

VELOCIDADE_FACIL = 300
VELOCIDADE_MEDIO = 200
VELOCIDADE_DIFICIL = 100

def alterar_dificuldade(dificuldade):
    config.dificuldade = dificuldade

    if dificuldade == 1:
        config.velocidade_jogador = VELOCIDADE_FACIL
        config.tempo_recarga = 400
    elif dificuldade == 2:
        config.velocidade_jogador = VELOCIDADE_MEDIO
        config.tempo_recarga = 500
    elif dificuldade == 3:
        config.velocidade_jogador = VELOCIDADE_DIFICIL
        config.tempo_recarga = 600

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

    if uteis.clicou(botao_facil):
        alterar_dificuldade(1)
        config.estado = "jogo"
    elif uteis.clicou(botao_medio):
        alterar_dificuldade(2)
        config.estado = "jogo"
    elif uteis.clicou(botao_dificil):
        alterar_dificuldade(3)
        config.estado = "jogo"


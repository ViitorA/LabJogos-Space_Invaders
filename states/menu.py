import config
from PPlay.sprite import *
from utils import clicou

def menu():
    config.janela.set_background_color([20,10,80])

    botao_jogar = Sprite("assets/jogar.png")
    botao_jogar.set_position( (config.janela.width - botao_jogar.width)/2, 20)

    botao_dificuldades = Sprite("assets/dificuldade.png")
    botao_dificuldades.set_position( (config.janela.width - botao_dificuldades.width)/2, 40+120)

    botao_ranking = Sprite("assets/ranking.png")
    botao_ranking.set_position( (config.janela.width - botao_dificuldades.width)/2, 60+240)

    botao_sair = Sprite("assets/sair.png")
    botao_sair.set_position( (config.janela.width - botao_sair.width)/2, 80+360)

    botao_jogar.draw()
    botao_dificuldades.draw()
    botao_ranking.draw()
    botao_sair.draw()

    if clicou(botao_jogar):
        config.estado = "jogo"
    elif clicou(botao_dificuldades):
        config.estado = "dificuldades"
    elif clicou(botao_ranking):
        config.estado = "ranking"
    elif clicou(botao_sair):
        config.janela.close()
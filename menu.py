import config

from utils import clicou

def menu(sprites):
    config.janela.set_background_color([20,10,80])

    botao_jogar = sprites["botao_jogar"]
    botao_jogar.set_position( (config.janela.width - botao_jogar.width)/2, 20)

    botao_dificuldades = sprites["botao_dificuldades"]
    botao_dificuldades.set_position( (config.janela.width - botao_dificuldades.width)/2, 40+120)

    botao_ranking = sprites["botao_ranking"]
    botao_ranking.set_position( (config.janela.width - botao_dificuldades.width)/2, 60+240)

    botao_sair = sprites["botao_sair"]
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
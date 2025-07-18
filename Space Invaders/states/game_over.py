import datetime
import pygame
import config
import states.ranking as ranking
import states.jogo as jogo
import player

def show():
    config.janela.set_background_color([80,10,40])

    # Uso algumas funções do pygame para poder achar as dimensões do texto renderizado p/a centralizá-lo
    text_surface = pygame.font.SysFont('Tahoma', 50).render("GAME OVER", True, (255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.centerx = config.janela.width // 2
    text_rect.centery = config.janela.height // 2

    config.janela.draw_text("GAME OVER", text_rect.x, text_rect.y, size = 50, color = (255,255,255), font_name = 'Tahoma', bold = True, italic = False) 
        
    config.janela.update()

    print("Qual é seu nome? ")
    player_name = input()
    ranking.ranking_organizado = False

    with open("Space Invaders/ranking.txt", "at") as f: # o 'with' automaticamente fecha o arquivo
        f.write(player_name.upper() + '\n')
        f.write(str(player.pontos) + '\n')
        f.write(str(datetime.datetime.now()) + '\n')

    config.estado = "menu"
    jogo.resetar_variaveis()
    player.pontos = 0
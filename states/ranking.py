from pathlib import Path
import pygame
import config

YELLOW = (200,100,0)
THICKNESS = 10

CAMINHO = Path("ranking.txt")

ranking_organizado = False

def ordenar_ranking(file, linhas):
    dados = []
    for i in range(0, len(linhas), 3):
        if i + 2 < len(linhas): # Garante que há bloco completo
            nome = linhas[i]
            pontos = int(linhas[i + 1])
            data = linhas[i + 2]
            dados.append((nome,pontos,data))

    dados_ordenados = sorted(dados, key=lambda x: x[1], reverse = True)
    for nome, pontos, data in dados_ordenados:
        file.write(f"{nome}\n{pontos}\n{data}\n")

    global ranking_organizado
    ranking_organizado = True


def mostrar_ranking():
    config.janela.set_background_color([20,10,80])

    window_w = config.janela.width
    window_h = config.janela.height
    # BORDA SUPERIOR
    pygame.draw.rect(config.janela.get_screen(), YELLOW, (30, 50, window_w - 60, THICKNESS))
    
    # BORDA ESQUERDA
    pygame.draw.rect(config.janela.get_screen(), YELLOW, (20, 60, THICKNESS, window_h - 120))
    # BORDA DIREITA
    pygame.draw.rect(config.janela.get_screen(), YELLOW, (window_w - 30, 60, THICKNESS, window_h - 120))

    # BORDA INFERIOR
    pygame.draw.rect(config.janela.get_screen(), YELLOW, (30, window_h - 60, window_w - 60, THICKNESS))

    # Define a área onde será escrito o ranking
    area = (20 + THICKNESS, # x0
            50 + THICKNESS, # y0
            window_w - 30,  # x
            window_h - 60   # y
            )  

    if CAMINHO.is_file():
        with open(CAMINHO) as f:
            linhas = f.readlines()
            linhas = [linha.strip() for linha in linhas]
        
        global ranking_organizado
        if not ranking_organizado:
            with open(CAMINHO, "wt") as f:
                ordenar_ranking(f, linhas)
        with open(CAMINHO) as f:
            j = 1
            for i in range(0, len(linhas), 3): # Mostra os 5 primeiros colocados
                if (i + 2 < len(linhas) and i <= 14): # Garante que há bloco completo
                    nome = linhas[i]
                    pontos = linhas[i+1]
                    data = linhas[i+2]
                    user_rank = str(j) + ' - ' + nome + '\tPTS ' + pontos + '\t' + data
                    config.janela.draw_text(user_rank, area[0] + 10, area[1] + i * 10, size = 30, color = YELLOW, font_name = 'Tahoma', bold = False, italic = False)
                    j += 1

    else:
        text_surface = pygame.font.SysFont('Tahoma', 50).render("SEM JOGADORES", True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.centerx = (area[2] - area[0]) // 2
        text_rect.centery = (area[3] - area[1]) // 2

        config.janela.draw_text("SEM JOGADORES", text_rect.x, text_rect.y, size = 50, color = YELLOW, font_name = 'Tahoma', bold = True, italic = False) 
            

    if config.teclado.key_pressed("ESC"):
        config.estado = "menu"
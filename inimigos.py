from PPlay.sprite import *
import config
import jogo

def spawn(x, y, m, n):
    largura = Sprite("assets/inimigo.png").width
    altura = Sprite("assets/inimigo.png").height
    gap_x = largura // 2
    gap_y = altura // 2

    for linha in range(n):
        for coluna in range(m):
            inimigo = {
                "sprite": Sprite("assets/inimigo.png"),
                "x": x + (largura + gap_x) * coluna,
                "y": y + (altura + gap_y) * linha,
                "velocidade": 200
            }
            jogo.lista_inimigos.append(inimigo)

def move_todos(lista_inimigos, delta_t):
    # Descobrir se algum inimigo bateu na borda
    descer = False
    inverter = False

    for inimigo in lista_inimigos:
        novo_x = inimigo["x"] + inimigo["velocidade"] * delta_t
        if novo_x + inimigo["sprite"].width >= config.janela.width or novo_x <= 0:
            descer = True
            inverter = True
            break

    # Se algum bateu, todos descem e invertem velocidade
    if descer:
        for inimigo in lista_inimigos:
            inimigo["y"] += 70
            inimigo["velocidade"] *= -1

    # Agora move todos normalmente
    for inimigo in lista_inimigos:
        inimigo["x"] += inimigo["velocidade"] * delta_t

def draw(inimigo):
    inimigo["sprite"].set_position(inimigo["x"], inimigo["y"])
    inimigo["sprite"].draw()
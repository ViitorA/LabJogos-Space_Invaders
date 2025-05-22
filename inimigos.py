import config
import jogo

def spawn(sprites, x, y, colunas, linhas):
    inimigo = {
        "type": "inimigo",
        "x": x,
        "y": y,
        "x1": x + sprites["inimigo"].width * colunas + (sprites["inimigo"].width//2) * (colunas - 1), # largura da matriz de sprites
        "velocidade": 200,
        "direcao": "direita",

        "sprites": [[sprites["inimigo"] for _ in range(colunas)] for _ in range(linhas)] 
    }

    print("x: " + str(inimigo["x"]))
    print("x1: " + str(inimigo["x1"]))

    jogo.lista_objetos.append(inimigo)

def move(inimigo, delta_t):
    inimigo["x"] += inimigo["velocidade"] * delta_t
    inimigo["x1"] += inimigo["velocidade"] * delta_t

    # TODO: arrumar a descida dos monstros, o problema ou tá aqui ou no desenhar_objeto
    if inimigo["x1"] >= config.janela.width:
        inimigo["y"] += 5
        inimigo["velocidade"] *= -1
    if inimigo["x"] <= 0:
        inimigo["y"] += 5
        inimigo["velocidade"] *= -1

def draw(inimigo):
    j = 0
    
    for linha in inimigo["sprites"]:
        i = 0

        for sprite in linha:
            sprite.set_position(inimigo["x"] + (sprite.width + sprite.width/2) * i, inimigo["y"] + (sprite.height + sprite.height/2) * j)
            sprite.draw()
            i += 1
            
        j += 1
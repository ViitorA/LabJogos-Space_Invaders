import config
import jogo

def spawn(sprites, x, y, m, n):
    inimigo = {
        "type": "inimigo",
        "x": x,
        "y": y,
        "x1": x + sprites["inimigo"].width * m + (sprites["inimigo"].width//2) * (m - 1), # largura da matriz de sprites
        "y1": y + sprites["inimigo"].height * n + (sprites["inimigo"].height//2) * (n - 1), # altura da matriz de sprites
        "velocidade": 200,

        "sprites": [[sprites["inimigo"] for _ in range(m)] for _ in range(n)] 
    }
    jogo.lista_objetos.append(inimigo)

def move(inimigo, delta_t):
    # move os inimigos 
    inimigo["x"] += inimigo["velocidade"] * delta_t
    inimigo["x1"] += inimigo["velocidade"] * delta_t

    if inimigo["x1"] >= config.janela.width:
        # Precisa fazer isso para a condicional não contar várias vezes 
        inimigo["x"] -= 2
        inimigo["x1"] -= 2

        # Quando os inimigos tocam no lado eles abaixam 70px
        inimigo["y"] += 70
        inimigo["y1"] += 70
        inimigo["velocidade"] *= -1 # Inverte o movimento
    if inimigo["x"] <= 0:
        inimigo["x"] += 2
        inimigo["x1"] += 2

        inimigo["y"] += 70
        inimigo["y1"] += 70
        inimigo["velocidade"] *= -1


def draw(inimigo):
    j = 0
    
    for linha in inimigo["sprites"]:
        i = 0

        for sprite in linha:
            # Faz o cálculo da posição de cada sprite a partir do tamanho dos sprites e o tamanho do gap multiplicado pelo index do sprite na matriz
            x = inimigo["x"] + (sprite.width + sprite.width/2) * i
            y = inimigo["y"] + (sprite.height + sprite.height/2) * j

            sprite.set_position(x,y)
            sprite.draw()
            i += 1
            
        j += 1

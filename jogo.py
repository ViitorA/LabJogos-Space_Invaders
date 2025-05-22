from PPlay.sprite import *

import config

lista_objetos = []
inimigo_spawnado = False

def spawnar_tiro(sprites, x,y, owner):
    tiro = {
        "type": "tiro",
        "x": x,
        "y": y
    }

    match owner:
        case "jogador":
            tiro["owner"] = "jogador"
            tiro["sprite"] = sprites["tiro-jogador"]
            tiro["height"] = sprites["tiro-jogador"].height
            tiro["width"] = sprites["tiro-jogador"].width
        case "inimigo":
            tiro["owner"] = "inimigo"

    lista_objetos.append(tiro)

def spawnar_inimigos(sprites, x, y, colunas, linhas):
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

    lista_objetos.append(inimigo)

def atualizar_objeto(objeto, delta_t):
    if objeto["type"] == "tiro":
        if objeto["y"] < 0 - objeto["height"]:
            lista_objetos.remove(objeto)
        
        if objeto["owner"] == "jogador":
            objeto["y"] -= 200 * delta_t
        elif objeto["owner"] == "inimigo":
            objeto["y"] += 200 * delta_t  
    elif objeto["type"] == "inimigo":
        objeto["x"] += objeto["velocidade"] * delta_t
        objeto["x1"] += objeto["velocidade"] * delta_t

        # TODO: arrumar a descida dos monstros, o problema ou tá aqui ou no desenhar_objeto
        if objeto["x1"] >= config.janela.width:
            objeto["y"] += 5
            objeto["velocidade"] *= -1
        if objeto["x"] <= 0:
            objeto["y"] += 5
            objeto["velocidade"] *= -1

def desenhar_objeto(objeto):
    if objeto["type"] == "inimigo":
        j = 0
        for linha in objeto["sprites"]:
            i = 0

            for sprite in linha:
                sprite.set_position(objeto["x"] + (sprite.width + sprite.width/2) * i, objeto["y"] + (sprite.height + sprite.height/2) * j)
                sprite.draw()
                i += 1
            
            j += 1
    else:
        objeto["sprite"].set_position(objeto["x"], objeto["y"])
        objeto["sprite"].draw()

def jogo(sprites):
    delta_t = config.janela.delta_time()
    tempo_atual = pygame.time.get_ticks()

    player = sprites["player"]
    global ultimo_tiro

    # SPAWNA INIMIGOS
    global inimigo_spawnado
    if not inimigo_spawnado:
        spawnar_inimigos(sprites, 10, 10, 4, 3)
        inimigo_spawnado = True

    if not config.game_started:
        player.set_position( (config.janela.width-player.width)/2, config.janela.height-player.height-20)
        ultimo_tiro = 0.0
        config.game_started = True

    config.janela.set_background_color([20,10,40])
    
    if config.teclado.key_pressed("ESC"):
        config.estado = "menu"
    
    if config.teclado.key_pressed("A") and player.x > 0:
        player.x -= config.velocidade_jogador * delta_t
    elif config.teclado.key_pressed("D") and player.x + player.width < config.janela.width:
        player.x += config.velocidade_jogador * delta_t
    
    if config.teclado.key_pressed("SPACE") and tempo_atual - ultimo_tiro > config.tempo_recarga:
        spawnar_tiro(sprites, player.x + player.width/2, player.y - 10, "jogador")
        ultimo_tiro = pygame.time.get_ticks()

    for objeto in lista_objetos:
        atualizar_objeto(objeto, delta_t)
        desenhar_objeto(objeto)

    player.draw()
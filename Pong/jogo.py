from PPlay.window import *
from PPlay.sprite import *
from PPlay.collision import *

def init():
    # JANELA
    global janela
    janela = Window(1200,800)
    janela.set_title("Victor Alexander")

    # TECLADO
    global teclado
    teclado = janela.get_keyboard()

    # PLACAR
    global pontos_jogador
    pontos_jogador = 0
    global pontos_oponente
    pontos_oponente = 0

    init_objetos()

def init_objetos():
    global bolinha
    bolinha = Sprite("Pong/assets/bolinha.png", frames=1);   
    bolinha.set_position( (janela.width/2)-(bolinha.width) , (janela.height/2)-(bolinha.height))

    global pad_oponente
    pad_oponente = Sprite("Pong/assets/pad.png", frames=1)
    pad_oponente.set_position(15, (janela.height/2)-(pad_oponente.height/2))

    global pad_jogador
    pad_jogador = Sprite("Pong/assets/pad.png", frames=1)
    pad_jogador.set_position(janela.width-pad_jogador.width-15, (janela.height/2)-(pad_oponente.height/2))

init()

start = False

vel_bolinha_x = 0
vel_bolinha_y = 0
oponente_vel = 0

VEL_MAX = 700

while True:
    delta_t = janela.delta_time()
    
    if teclado.key_pressed("SPACE") and not start:
        vel_bolinha_x = -500
        vel_bolinha_y = -500
        oponente_vel = 450

        start = True

    # MOVIMENTAÇÃO DO JOGADOR
    if(teclado.key_pressed("UP") and pad_jogador.y > 0):
        pad_jogador.y -= 500 * delta_t
    elif(teclado.key_pressed("DOWN") and pad_jogador.y + pad_jogador.height < janela.height):
        pad_jogador.y += 500 * delta_t

    # MOVIMENTAÇÃO IA
    if( bolinha.y + bolinha.height/2 > pad_oponente.y + pad_oponente.height/2): pad_oponente.y += oponente_vel * 0.8 * delta_t
    if( bolinha.y + bolinha.height/2 < pad_oponente.y + pad_oponente.height/2): pad_oponente.y -= oponente_vel * 0.8 * delta_t


    # COLISÃO BOLINHA-PAD
    if pad_oponente.collided(bolinha):
        if vel_bolinha_x <= VEL_MAX or vel_bolinha_x >= -VEL_MAX:
            bolinha.x = 15 + pad_oponente.x + pad_oponente.width + 1
            vel_bolinha_x *= -1.05
        else:
            bolinha.x = 15 + pad_oponente.x + pad_oponente.width + 1
            vel_bolinha_x *= -1

    if pad_jogador.collided(bolinha):
        if vel_bolinha_x <= VEL_MAX or vel_bolinha_x >= -VEL_MAX: 
            #bolinha.x = janela.width - pad_jogador.width - 15
            vel_bolinha_x *= -1.05
        else:
            #bolinha.x = janela.width - pad_jogador.width - 15
            vel_bolinha_x *= -1

    # MOVIMENTO BOLINHA
    bolinha.x += vel_bolinha_x  * delta_t
    bolinha.y += vel_bolinha_y * delta_t

    if bolinha.y <= 0:
        vel_bolinha_y *= -1
        bolinha.y = 1
    if bolinha.y + bolinha.height >= janela.height:
        vel_bolinha_y *= -1
        bolinha.y = janela.height-bolinha.height -1


    # COLISÃO BOLINHA-CANTOS
    if bolinha.x + bolinha.width >= janela.width + pad_jogador.width:
        vel_bolinha_x = 0
        vel_bolinha_y = 0
        oponente_vel = 0 

        bolinha.set_position( (janela.width/2)-(bolinha.width) , (janela.height/2)-(bolinha.height))
        pad_oponente.set_position(15, (janela.height/2)-(pad_oponente.height/2))
        pad_jogador.set_position( janela.width-pad_jogador.width-15, (janela.height/2)-(pad_jogador.height/2))

        start = False
        pontos_oponente += 1

    if bolinha.x <= 0:
        vel_bolinha_x = 0
        vel_bolinha_y = 0
        oponente_vel = 0

        bolinha.set_position( (janela.width/2)-(bolinha.width) , (janela.height/2)-(bolinha.height))
        pad_oponente.set_position(15, (janela.height/2)-(pad_oponente.height/2))
        pad_jogador.set_position( janela.width-pad_jogador.width-15, (janela.height/2)-(pad_jogador.height/2))

        start = False
        pontos_jogador += 1


# ATUALIZA
    janela.set_background_color([0,0,255])

    bolinha.draw() 
    pad_jogador.draw()
    pad_oponente.draw()

    # Exibe o placar
    janela.draw_text(str(pontos_oponente), (janela.width/4), (janela.height/5),size=70, color=(255,100,0), font_name= '', bold=False, italic=False)
    janela.draw_text(str(pontos_jogador), 3*(janela.width/4), (janela.height/5),size=70, color=(255,100,0), font_name= '', bold=False, italic=False)

    janela.update() # Swap buffer

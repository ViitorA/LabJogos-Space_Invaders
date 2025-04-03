from PPlay.window import *
from PPlay.sprite import *

JANELA_X = 1000
JANELA_Y = 500

def inicializar():
    global janela;
    janela = Window(JANELA_X,JANELA_Y)
    janela.set_title("Victor Alexander")

inicializar()

# Inicializar bolinha dentro ou fora do loop?
bolinha = Sprite("assets/bolinha.png", frames=1);   

while True:
    janela.set_background_color([0,0,255])

    bolinha.set_position(JANELA_X/2,JANELA_Y/2)
    bolinha.draw() 

    janela.update()

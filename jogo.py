from PPlay.window import *
from PPlay.sprite import *

def inicializar():
    global janela;
    janela = Window(1000,500)
    janela.set_title("Victor Alexander")
   
    global teclado
    teclado = janela.get_keyboard()

    init_bolinha()

def init_bolinha():
    global bolinha 
    bolinha = Sprite("assets/bolinha.png", frames=1);   
    bolinha.set_position( (janela.width/2)-(bolinha.width) , (janela.height/2)-(bolinha.height))


inicializar()

vetor_velocidade_x = 1
vetor_velocidade_y = 1
VELOCIDADE_MAXIMA = 5

start = False

while True:
    janela.set_background_color([0,0,255])

    bolinha.draw() 
    
    if(teclado.key_pressed("space")): start = True

    if(start):
        if(bolinha.x + bolinha.width > janela.width or bolinha.x < 0):
            if(vetor_velocidade_x > VELOCIDADE_MAXIMA or vetor_velocidade_x < -VELOCIDADE_MAXIMA):
                vetor_velocidade_x *= -1
            else:
                vetor_velocidade_x *= -1.2
    
        if(bolinha.y + bolinha.height > janela.height or bolinha.y < 0):
            vetor_velocidade_y *= -1
        
        bolinha.x += vetor_velocidade_x
        bolinha.y += vetor_velocidade_y

    janela.update() # Swap buffer

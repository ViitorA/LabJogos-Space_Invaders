import config

def mostrar_ranking():
    while True:
        # VISUAL
        config.janela.set_background_color([15,0,25])

        config.janela.update()
        
        # LÓGICA
        if config.teclado.key_pressed("ESC"):
            config.CONTROLADOR = config.MENU
            return 0
import config

def iniciar_jogo():
    while True:
        # VISUAL
        config.janela.set_background_color([0,0,0])
        config.janela.update()

        # LÓGICA
        if config.teclado.key_pressed("ESC"):
            config.CONTROLADOR = config.MENU
            return 0

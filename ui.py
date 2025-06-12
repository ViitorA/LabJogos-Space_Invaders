import config
import player

def mostrar_ui():
    config.janela.draw_text(str(player.vida), 10, 10, size=50, color = (255,255,255), font_name = "Tahoma")
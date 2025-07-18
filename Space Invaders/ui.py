import config
import player

def mostrar_ui():
    # VIDA
    config.janela.draw_text(str(player.vida), 10, config.janela.height - 55, size=50, color = (255,255,255), font_name = "Tahoma")

    # PONTOS
    milhar = player.pontos//1000
    centena = (player.pontos % 1000) // 100
    dezena =  (player.pontos % 100) // 10
    config.janela.draw_text('0', config.janela.width - 40, 10, size = 40, color = (255,255,255), font_name = "Tahoma")
    config.janela.draw_text(str(dezena), config.janela.width - 80,   10, size = 40, color = (255,255,255), font_name = "Tahoma")
    config.janela.draw_text(str(centena), config.janela.width - 120, 10, size = 40, color = (255,255,255), font_name = "Tahoma")
    config.janela.draw_text(str(milhar), config.janela.width - 160,  10, size = 40, color = (255,255,255), font_name = "Tahoma")
    
    

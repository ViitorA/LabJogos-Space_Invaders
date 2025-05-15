# DIFICULDADE
# FÁCIL - 1
# MÉDIO - 2
# DIFICIL - 3
global dificuldade
dificuldade = 1

global janela
global teclado

global mouse

# Se isso não for implementado, um único clique do mouse pode apertar múltiplos botões em múltiplas telas caso estejam na mesma posição. Ou seja, é feito para limitar a quantidade de cliques por milisegundo. 
# Ao apertar um botão, ele irá verificar a condição: tempo_atual - ultimo_clique > delay_entre_cliques
# onde tempo_atual = pygame.time.get_ticks()
#      ultimo_clique = tempo_atual
#      delay_entre_cliques = 300 (constante)
global ultimo_clique
global delay_entre_cliques
delay_entre_cliques = 300

# O controlador controla(kk) o estado atual do jogo(em que cenário/janela ele se encontra)
global CONTROLADOR

# ESTADOS DO JOGO
global MENU
MENU = 0

global JOGO
JOGO = 1

global DIFICULDADES 
DIFICULDADES = 2

global RANKING
RANKING = 3

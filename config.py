# DIFICULDADE
# FÁCIL - 1
# MÉDIO - 2
# DIFICIL - 3
global dificuldade
dificuldade = 1

global janela
global teclado

global mouse

# Se isso não for implementado, um único clique do mouse pode apertar múltiplos botões em uma mesma posição entre múltiplas janelas. Exemplo: Eu aperto o botão de 
# 'dificuldades' no menu, quando eu aperto isso ao mesmo tempo ele vai apertar a dificuldade 'médio' pois a troca de janela foi tão rápida e foi registrado tantos 
# cliques(mesmo tendo apertado somente uma vez) que ele aperta automaticamente outro botão.
# Logo, ao apertar um botão, ele irá verificar a condição: tempo_atual - ultimo_clique > delay_entre_cliques
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

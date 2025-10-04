"""
Módulo jogador
Gerencia posição, movimento e pontuação do jogador.
"""
def iniciar_jogador():
    return [0, 0], 0

def mover(lab, posicao, direcao):
    x, y = posicao
    tamanho = len(lab)
    if direcao == 'w' and x > 0 and lab[x-1][y] != '#':
        x -= 1
    elif direcao == 's' and x < tamanho-1 and lab[x+1][y] != '#':
        x += 1
    elif direcao == 'a' and y > 0 and lab[x][y-1] != '#':
        y -= 1
    elif direcao == 'd' and y < tamanho-1 and lab[x][y+1] != '#':
        y += 1
    return [x, y]

def pontuar(pontos):
    return pontos + 10

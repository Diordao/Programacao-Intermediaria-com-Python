"""
Módulo jogador.py - Controla o jogador e a pontuação
"""

def iniciar_jogador():
    """Define a posição inicial e pontuação"""
    return {"pos": [0, 0], "pontos": 0}

def mover(jogador, direcao, tamanho=5):
    """Move o jogador de acordo com a direção"""
    x, y = jogador["pos"]
    match direcao:
        case "w":
            x = max(0, x - 1)
        case "s":
            x = min(tamanho - 1, x + 1)
        case "a":
            y = max(0, y - 1)
        case "d":
            y = min(tamanho - 1, y + 1)
    jogador["pos"] = [x, y]
    return jogador

def pontuar(jogador):
    """Aumenta a pontuação"""
    jogador["pontos"] += 10
    return jogador

def animar_vitoria(n):
    """Função recursiva que imprime uma contagem regressiva de vitória"""
    if n == 0:
        print("🎉 Vitória!")
        return
    print(f"🎊 Parabéns! {n}")
    animar_vitoria(n - 1)
